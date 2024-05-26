from tinyspline import *
from Shape import Shape

class BSpline:

    def __init__(self, ctrlp:list, knots:list, degree:int, type:int = 1):

        # Controlli preliminari
        if((len(ctrlp) + degree + 1 != len(knots)) or (not type in [0,1,2])):
            raise IndexError("Invalid parameters")

        _type = None
        if(type == 0):
            _type = tinyspline.BSpline.Opened
        elif(type == 1):
            _type = tinyspline.BSpline.Clamped
        elif(type == 2):
            _type = tinyspline.BSpline.Beziers

        self.__bSpline = tinyspline.BSpline(len(ctrlp), 2, degree, _type)

        _ctrlp = self.__bSpline.control_points
        for i, ele in enumerate(ctrlp):
            _ctrlp[i*2] = ele[0]
            _ctrlp[i*2 + 1] = ele[1]
        self.__bSpline.control_points = _ctrlp

        _knots = self.__bSpline.knots
        for i, ele in enumerate(knots):
            _knots[i] = ele
        self.__bSpline.knots = _knots
        
        self.__BSplineShape = []

        self.__Shape = []


    def CalcBSplineShape(self, resolution:float = 0.0001):

        if((resolution <= 0 or resolution >= 1)):
            self.__BSplineShape = []
            self.__Shape = []
            return None

        _knots = self.__bSpline.knots
        resolution = _knots[-1] * resolution
        
        i = 0

        _curve = []

        while(i <= _knots[-1]):
            result = self.__bSpline.eval(i).result
            _curve.append([result[0], result[1]])
            i += resolution

        self.__BSplineShape = []

        for point in _curve:
            if point not in self.__BSplineShape:
                self.__BSplineShape.append(point)

        return None

    
    def CalcShape(self, ptMinDist:float, angTollerance:int = 3):

        if((angTollerance < 1) or (angTollerance > 179)):
            self.__Shape = []

        shape = Shape(self.__BSplineShape, angTollerance)

        self.__Shape = shape.Generate(ptMinDist)

    @property
    def BSplineShape(self):
        return self.__BSplineShape
    
    @property
    def Shape(self):
        return self.__Shape
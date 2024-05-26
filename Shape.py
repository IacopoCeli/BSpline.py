import math;

class Shape:

    def __init__(self, points:list, angTollerance:int):

        self.__points = points # Lista di punti nel formato [x, y]

        # Cerco i vertici della figura
        #----------------------------------------------------------------------------------------------------------

        self.__vertex = []

        if(Shape.PointsDistanceCalc(self.__points[0], self.__points[-1]) < 0.1):
            i1 = len(self.__points) - 1
        else:
            i1 = 0

        i2 = ((i1 + 1) % (len(self.__points)))
        i3 = ((i2 + 1) % (len(self.__points)))

        # Analizzo i punti a tre a tre
        while(i2 < len(self.__points) - 1):

            m1 = Shape.AngCoeffCalc(pt1=self.__points[i2], pt2=self.__points[i1]) # Calcolo coefficiente angolare tra pt1 e pt2
            m2 = Shape.AngCoeffCalc(pt1=self.__points[i3], pt2=self.__points[i2]) # Calcolo coefficiente angolare tra pt2 e pt3
            m = abs((m1 - m2) / (1 + m1 * m2)) # Calcolo la mutua posizione tra le due rette definite dai tre punti
            ang = math.atan(m) * 360 * 1/(2*math.pi) # Calcolo l'angolo compreso tra le due rette

            if(ang > angTollerance): # Se l'angolo compreso supera la tolleranza impostata il punto identificato dall'incontro delle due rette è un vertice
                self.__vertex.append(i2)

            i1 = ((i1 + 1) % (len(self.__points)))
            i2 = ((i2 + 1) % (len(self.__points)))
            i3 = ((i3 + 1) % (len(self.__points)))

        if(len(self.__vertex) == 0):
            self.__vertex.append(0)
            self.__vertex.append(len(self.__points) - 1)
        else:
            self.__vertex.append(self.__vertex[0])

        #----------------------------------------------------------------------------------------------------------
    
    def Generate(self, ptMinDist:float):
        
        curve = []

        index = self.__vertex[0]

        for i, ele in enumerate(self.__vertex):

            if(i != 0):

                D = self.__LenghtCalc(index, ele) # Lunghezza totale della porzione di figura racchiusa tra due vertici
                index = ele

                N = math.trunc(D/ptMinDist) # Numero di punti con cui definire la porzione di figura
                r = D % ptMinDist # Resto dalla divisione della porzione di figura
                g = r/N # residuo da aggiungere ad ogni punto
                t = (g/ptMinDist)*100 # differenza percentuale per un eventuale confronto di tolleranza 
                d = ptMinDist + g # effettiva distanza tra due punti

                p = 1 # Punto del risultato attualmente ricercato
                s = self.__vertex[i-1] # punto della curva attualmente analizzato
                dd = 0 # Distanza attualmente percorsa

                inibith = False

                curve.append(self.__points[s])

                while(s != ele):

                    if(not inibith):
                        dd += Shape.PointsDistanceCalc(self.__points[s], self.__points[(s + 1) % (len(self.__points))])

                    if(dd == p*d):
                        p += 1
                        if(p <= N):
                            curve.append(self.__points[s+1])
                        
                    elif (dd > p*d):
                        p += 1
                        if(p <= N):
                            newPt = Shape.NextPoint(self.__points[s], self.__points[s+1], (dd - (p-1)*d))
                            curve.append(newPt)
                        

                    if(dd < p*d):
                        s = (s + 1) % (len(self.__points))
                        inibith = False
                    else:
                        inibith = True

        curve.append(self.__points[self.__vertex[-1]])

        return curve

    def __LenghtCalc(self, iStart:int, iStop:int):
        D:float = 0

        i = iStart

        while(i != iStop):
            D += Shape.PointsDistanceCalc(self.__points[i], self.__points[(i + 1) % (len(self.__points))])
            i = (i + 1) % (len(self.__points))

        return D

    @staticmethod            
    def AngCoeffCalc(pt1:list, pt2:list):

        limit = 1000

        if(pt1[0] == pt2[0]):
            return limit
        
        else:

            m = (pt2[1] - pt1[1])/(pt2[0] - pt1[0])

            if(abs(m) > limit):
                return limit
            else:
                return m
    
    @staticmethod            
    def InterceptCalc(pt1:list, pt2:list):

        m = Shape.AngCoeffCalc(pt1, pt2)

        return pt1[1] - m * pt1[0]

    @staticmethod            
    def PointsDistanceCalc(pt1:list, pt2:list):
        return math.sqrt(math.pow((pt2[0]-pt1[0]),2) + math.pow((pt2[1]-pt1[1]),2))

    @staticmethod
    def NextPoint(pt1:list, pt2:list, distance:float):

        x1 = pt1[0]
        y1 = pt1[1]
        x2 = pt2[0]
        y2 = pt2[1]
        m = Shape.AngCoeffCalc(pt1, pt2)
        q = Shape.InterceptCalc(pt1, pt2)
        res = [0, 0]

        # Caso in cui i due punti sono uguali
        if(pt1 == pt2):
            return pt1
        
        # Caso in cui i due punti stanno su una retta perpendicolare
        if(math.trunc(x1*10)/10 == math.trunc(x2*10)/10):
            res[0] = x1
            if(y1 < y2):
                res[1] = y2 - distance
            else:
                res[1] = y2 + distance
        else:
            if(x1 < x2):
                res[0] = ((2*m*y2+2*x2-2*m*q)-(math.sqrt(math.pow((2*m*q-2*x2-2*m*y2),2)-4*(1+math.pow(m,2))*(math.pow(x2,2)+math.pow(y2,2)+math.pow(q,2)-2*q*y2-math.pow(distance,2)))))/(2*(1+math.pow(m,2)))
            else:
                res[0] = ((2*m*y2+2*x2-2*m*q)+(math.sqrt(math.pow((2*m*q-2*x2-2*m*y2),2)-4*(1+math.pow(m,2))*(math.pow(x2,2)+math.pow(y2,2)+math.pow(q,2)-2*q*y2-math.pow(distance,2)))))/(2*(1+math.pow(m,2)))
            res[1] = res[0] * m + q

        return res

        
            
        

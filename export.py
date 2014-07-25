# coding=utf-8
import ofevent

#Objet,Date de début,Heure de début,Date de fin,Heure de fin,Toute la journée,Description,Lieu,Privé
#Examen final,12/05/20,19:10,12/05/07,22:00,False,Deux sujets de dissertation ayant trait aux questions traitées au cours du semestre,"University of Columbia, Salle Schermerhorn 614",True

CSV_HEADER= "\"Subject\",\"Start Date\",\"Start Time\",\"End Date\",\"End Time\",\"All day event\",\"Location\""

EVT_PLACE="Aérodrome de Toussus-le-Noble"

################################################################################
def guill(s):
    return "\"" + s + "\""

class CsvExport:
    @staticmethod
    def csv_objet(ofevt):
        return "Vol " + ofevt._plane
    
    @staticmethod
    def evt2csvline( ofevt):
        line=[ CsvExport.csv_objet(ofevt), ofevt._date_start, ofevt._t_start, \
               ofevt._date_end, ofevt._t_end, "False", EVT_PLACE ]
        line = map( guill, line)
        return ','.join(line)
    
    @staticmethod
    def action2csvline(ofaction):
        return CsvExport.evt2csvline(ofaction._evt1) if \
                ofaction._action==ofevent.ActionType.CONFIRM else None
    
    @staticmethod
    def actions2csv(ofactions):
        ans = CSV_HEADER + "\n"
        for action in ofactions:
            line = CsvExport.action2csvline(action)
            if line is not None:
                ans += CsvExport.action2csvline(action) + "\n"
        return ans


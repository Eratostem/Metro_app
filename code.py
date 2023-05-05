
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton




BordeauxA = {"Le Haillan Rostand":["Les Pins"],"Les Pins":["Le Haillan Rostand","Frères Robinson"],"Frères Robinson":["Les Pins","Hôtel de ville Mérignac"],"Hôtel de ville Mérignac":["Frères Robinson","Pin Gallant"],"Pin Gallant":["Hôtel de ville Mérignac","Mérignac Centre"],"Mérignac Centre":["Pin Gallant","Lycée de Mérignac"],"Lycée de Mérignac":["Mérignac Centre","Quatre Chemin"],"Quatre Chemin":["Lycée de Mérignac","Pierre Mendès-France"],"Pierre Mendès-France": ["Quatre Chemin","Alfred de Vigny"],"Alfred de Vigny":["Pierre Mendès-France","Fontaine d'Arlac"],"Fontaine d'Arlac":["Alfred de Vigny","Peychotte"],"Peychotte":["Fontaine d'Arlac","François Mitterand"],"François Mitterand":["Peychotte","Saint-Augustin"],"Saint-Augustin":["François Mitterand","Hôpital Pellegrin"],"Hôpital Pellegrin":["Saint-Augustin","Stade Chaban-Delmas"],"Stade Chaban-Delmas":["Hôpital Pellegrin","Gaviniès"],"Gaviniès":["Stade Chaban-Delmas","Hôtel de Police"],"Hôtel de Police":["Gaviniès","St-Bruno Hôtel de Répion"],"St-Bruno Hôtel de Répion":["Hôtel de Police","Mériadeck"],"Mériadeck":["St-Bruno Hôtel de Répion","Palais de Justice"],"Palais de Justice":["Mériadeck","Hôtel de ville"],"Hôtel de ville":["Palais de Justice","Musée d'Aquitaine","Ste-Catherine","Gambetta-madd"],"Ste-Catherine":["Hôtel de ville","Place du Palais"],"Place du Palais":["Ste-Catherine","Porte de Bourgogne"],"Porte de Bourgogne":["Place du Palais","St-Michel","Place de la Bourse","Stalingrad"],"Stalingrad":["Porte de Bourgogne","Jardin Botanique"],"Jardin Botanique":["Stalingrad","Thiers Benauge"],"Thiers Benauge":["Jardin Botanique","Galin"],"Galin":["Thiers Benauge","Jean Jaurès"],"Jean Jaurès":["Galin","Cenon Gare"],"Cenon Gare":["Jean Jaurès","Carnot Mairie de Cenon"],"Carnot Mairie de Cenon":["Cenon Gare","Buttinière"],"Buttinière":["Carnot Mairie de Cenon","Iris","Palmer"],"Palmer":["Buttinière","Pelletan"],"Pelletan":["Palmer","La Morlette"],"La Morlette":["Pelletan","Jean Zay"],"Jean Zay":["La Morlette","La Marègue"],"La Marègue":["Jean Zay","Floirac Dravemont"],"Floirac Dravemont":["La Marègue"],"Iris":["Buttinière","Gravières"],"Gravières":["Iris","Bois Fleuri"],"Bois Fleuri":["Gravières","Lauriers"],"Lauriers":["Bois Fleuri","Mairie de Lormont"],"Mairie de Lormont":["Lauriers","Carriet"],"Carriet":["Mairie de Lormont","La Gardette Bassens Carbon Blanc"],"La Gardette Bassens Carbon Blanc":["Carriet"]}
BordeauxB = {"Berges de la Garonne":["Claveau"],"Claveau":["Berges de la Garonne","Brandenburg"],"Brandenburg":["Claveau","New York"],"New York":["Brandenburg","Rue Achard"],"Rue Achard":["New York","La Cité du Vin"],"La Cité du Vin":["Rue Achard","Les Hangars"],"Les Hangars":["La Cité du Vin","Cours du Médoc"],"Cours du Médoc":["Les Hangars","Chartrons"],"Chartrons":["Cours du Médoc","CAPC"],"CAPC":["Chartrons","Quinconces"],"Quinconces":["Jardin public","Fondaudège Muséum","CAPC","Place de la Bourse","Grand Théâtre"],"Grand Théâtre":["Quinconces","Gambetta-madd"],"Gambetta-madd":["Grand Théâtre","Hôtel de ville"],"Hôtel de ville":["Gambetta-madd","palais de Justice","Ste-Catherine","Musée d'Aquitaine"],"Musée d'Aquitaine":["Hôtel de ville","Victoire"],"Victoire":["Musée d'Aquitaine","St-Nicholas"],"St-Nicholas":["Victoire","Bergonié"],"Bergonié":["St-Nicholas","Barrière St-Genès"],"Barrière St-Genès":["Bergonié","Roustaing"],"Roustaing":["Barrière St-Genès","Talence Centre-Forum"],"Talence Centre-Forum":["Roustaing","Peixotto"],"Peixotto":["Talence Centre-Forum","Béthanie"],"Béthanie":["Peixotto","Arts et Métiers"],"Arts et Métiers":["Béthanie","François Bordes"],"François Bordes":["Arts et Métiers","Doyen Brus"],"Doyen Brus":["François Bordes","Montaigne Montesquieu"],"Montaigne Montesquieu":["Doyen Brus","Unitec"],"Unitec":["Montaigne Montesquieu","Saige"],"Saige":["Unitec","Bougnard"],"Bougnard":["Saige","Camponac Médiathèque","Châtaigneraie"],"Camponac Médiathèque":["Bougnard","Pessac Centre"],"Pessac Centre":["Camponac Médiathèque"],"Châtaigneraie":["Bougnard","Cap Métiers"],"Cap Métiers":["Châtaigneraie","Hôpital Haut-Lévêque"],"Hôpital Haut-Lévêque":["Cap Métiers","Gare Pessac Alouette"],"Gare Pessac Alouette":["Hôpital Haut-Lévêque","France Alouette"],"France Alouette":["Gare Pessac Alouette"]}
BordeauxC = {"Villenave Pyrénées": ["Villenave Centre-Pont de la Maye"], "Villenave Centre-Pont de La Maye": ["Villenave Pyrénées", "Lycée Václav Havel"],"Lycée Václav Havel": ["Villenave Centre-Pont de la Maye", "Parc de Mussonville"],"Parc de Mussonville": ["Lycée Václav Havel", "gare de Bègles"],"Gare de Bègles": ["Parc de Mussonville", "Calais Centujean"],"Calais Centujean": ["Gare de Bègles", "Stade Musard"],"Stade Musard": ["Calais Centujean", "La Belle Rose"],"La Belle Rose": ["Stade Musard", "Terres Neuves"],"Terres Neuves": ["La Belle Rose", "Carle Vernet"],"Carle Vernet": ["Terres Neuves", "Belcier"],"Belcier": ["Carle Vernet", "Gare Saint-Jean"],"Gare Saint-Jean": ["Belcier", "Tauzia"],"Tauzia": ["Gare Saint-Jean", "Ste-Croix"],"Ste-Croix": ["Tauzia", "St-Michel"],"St-Michel": ["Ste-Croix", "Porte de Bourgogne"],"Porte de Bourgogne": ["St-Michel", "Place du Palais", "Place de la Bourse", "Stalingrad"],"Place de la Bourse": ["porte de Bourgogne", "Quinconces"],"Quinconces": ["Place de la Bourse", "Jardin Public"],"Jardin Public": ["Quinconces", "Place Paul Doumer"],"Place Paul Doumer": ["Jardin Public", "Camille Godard"],"Camille Godard": ["Place Paul Doumer", "Émile Counord"],"Émile Counord": ["Camille Godard", "Grand Parc"],"Grand Parc": ["Émile Counord", "Place Ravezies - Le Bouscat"],"Place Ravezies - Le Bouscat": ["Grand Parc", "Cracovie"],"Cracovie": ["Place Ravezies - Le Bouscat", "Les Aubiers", "La Vache"], "Les Aubiers": ["Cracovie", "Berges du Lac"], "Berges du Lac": ["Les Aubiers", "Quarante Journaux"], "Quarante Journaux": ["Berges du Lac", "Palais des Congrès"], "Palais des Congrès": ["Quarante Journaux", "Parc des Expositions Stade Matmut-Atlantique"], "Parc des Expositions Stade Matmut-Atlantique": ["Palais des Congrès"], "La Vache": ["Cracovie", "Ausone"], "Ausone": ["Gare de Burges", "La Vache"], "Gare de Bruges": ["Ausone", "Frankton"], "Frankton": ["Gare de Blanquefort", "Gare de Bruges"],"Gare de Blanquefort": ["Frankton"]}
BordeauxD = {"Eysines Cantinolle": ["Les Sources"], "Les Sources": ["Eysines Cantinolle", "Eysines Centre"], "Eysines Centre": ["les Sources", "Picot"], "Picot": ["Eysines Centre", "Simone Veil"], "Simone Veil": ["Picot", "Hippodrome"], "Hippodrome": ["Simone Veil", "Sainte-Germaine"], "Sainte-Germaine": ["Hippodrome", "Les Écus"], "Les Écus": ["Sainte-Germaine", "Mairie du Bouscat"], "Mairie du Bouscat": ["Les Écus", "Calypso"], "Calypso": ["Mairie du Bouscat", "Courbet"], "Courbet": ["Calypso", "Barrière du Médoc"], "Barrière du Médoc": ["Courbet", "Croix de Seguey"], "Croix de Seguey": ["Barrière du Médoc", "Fondaudège Muséum"], "Fondaudège Muséum": ["Croix de Seguey", "Quinconces"], "Quinconces": ["Fondaudège Muséum", "Jardin Public", "CAPC", "Place de la Bourse", "Grand Théâtre"], "Place de la Bourse": ["Quinconces", "Porte de Bourgogne"], "Porte de Bourgogne": ["Place de la Bourse", "Place du Palais", "St-Michel","Stalingrad"], "St-Michel": ["Porte de Bourgogne", "Ste-Croix"], "Ste-Croix": ["St-Michel", "Tauzia"], "Tauzia": ["Ste-Croix", "Gare Saint-Jean"],"Gare Saint-Jean": ["Tauzia", "Belcier"],"Belcier": ["Gare Saint-Jean", "Carle Vernet"], "Carle Vernet": ["Belcier"]}
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

bord = Merge(BordeauxA,BordeauxB)
bord = Merge(bord,BordeauxC)
bord = Merge(bord,BordeauxD)


def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = float('inf')
    proximity = 0
    path = [[start]]
    print(path)
    while True:
        proximity +=1
        if proximity > 10000:
            break
        for station in path:
            branch = 0
            print(station[-1])
            for correspondance in graph[station[-1]]:
                #test if the new station wasn't pass trough already
                not_passed = True
                for i in station:
                    if i == correspondance:
                        not_passed = False
                if not_passed and branch >0: 
                    station2 = station
                    station2.append(correspondance)
                    
                    path.append(station2)
                if not_passed and branch ==0:
                    station.append(correspondance)
                    branch += 1
                    print(station)
                if correspondance == goal:
                    print(station)
                    return station
    print("fail")
    return "fail"

class Metro_App(QMainWindow):
    def __init__(self,graph):
        super().__init__()
        self.title = 'Train Station App'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 200
        self.initUI()
        self.graph = graph
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        dep_label = QLabel('Departure City:', self)
        dep_label.move(20, 20)
        self.dep_textbox = QLineEdit(self)
        self.dep_textbox.move(120, 20)
        self.dep_textbox.resize(250, 25)
        dest_label = QLabel('Destination City:', self)
        dest_label.move(20, 60)
        self.dest_textbox = QLineEdit(self)
        self.dest_textbox.move(120, 60)
        self.dest_textbox.resize(250, 25)
        calc_button = QPushButton('Calculate', self)
        calc_button.move(150, 100)
        calc_button.clicked.connect(self.calculate_shortest_path)
        self.show()
    def calculate_shortest_path(self):
        dep_city = self.dep_textbox.text()
        dest_city = self.dest_textbox.text()
        shortest_path = dijkstra(self.graph, dep_city, dest_city)
        result_label = QLabel(f'Shortest path from {dep_city} to {dest_city}: {shortest_path}', self)
        result_label.move(20, 140)
        result_label.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Metro_App(bord)
    sys.exit(app.exec_())



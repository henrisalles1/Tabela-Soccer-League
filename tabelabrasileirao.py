from operator import attrgetter

class Time:
    total_de_times = 0
    def __init__(self, time, jogos, vitorias, empates, gol_pro, gol_contra):
        self.time = time
        self.jogos = jogos
        self.pontos = vitorias*3 + empates
        self.vitorias = vitorias
        self.empates = empates
        self.derrotas = jogos - (vitorias + empates)
        self.gol_pro = gol_pro
        self.gol_contra = gol_contra
        self.saldo = gol_pro - gol_contra
        Time.total_de_times += 1

        # pontos > saldo > vitorias > -derrotas > gol_pro
    def __lt__(self, outro):
        if self.pontos != outro.pontos:
            return self.pontos < outro.pontos
        elif self.saldo != outro.saldo:
            return self.saldo < outro.saldo
        elif self.vitorias != outro.vitorias:
            return self.vitorias < outro.vitorias
        elif self.derrotas != outro.derrotas:
            return self.derrotas > outro.derrotas
        elif self.gol_pro != outro.gol_pro:
            return self.gol_pro < outro.gol_pro

    def __str__(self):
        return f'{self.time} - {self.pontos}P {self.vitorias}V {self.empates}E {self.derrotas}D {self.gol_pro}GP {self.gol_contra}GC {self.saldo}SG'

botafogo = Time('Bot',38,5,12,32,62)
coritiba = Time('cur',38,7,10,31,54)
goias = Time('goi',38,9,10,41,63)
vasco = Time('Vas',38,10,11,37,56)
fortaleza = Time('For',38,10,11,34,44)
sport = Time('Spo',38,12,6,31,50)
bahia = Time('bah',38,12,8,48,59)
atle_go = Time('ago',38,12,14,40,45)
corinthias = Time('Cor',38,13,12,45,45)
ceara = Time('Cea',38,14,10,54,51)
rb_braga = Time('RBB',38,13,14,50,40)
atle_pr = Time('APR',38,15,8,38,36)
santos = Time('san',38,14,12,52,51)
palmeiras = Time('pal',38,15,13,51,37)
gremio = Time('gre',38,14,17,53,40)
fluminense = Time('Flu',38,18,10,55,42)
sao_paulo = Time('spa',38,18,12,59,41)
atle_mg = Time('amg',38,20,8,64,45)
inter = Time('int',38,20,10,61,35)
flamengo = Time('fla',38,21,8,68,48)

lista_de_times = [inter,atle_mg,sao_paulo,fluminense,gremio,palmeiras,santos,atle_pr,rb_braga,flamengo,ceara,corinthias,atle_go,bahia,sport,fortaleza,vasco,goias,coritiba,botafogo]
for tabela in sorted(lista_de_times, reverse=True):
    print(tabela)

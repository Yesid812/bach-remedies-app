# engine.py
from experta import KnowledgeEngine, Fact, Rule, OR

class BachFlowersEngine(KnowledgeEngine):

    @Rule(OR(
        Fact(sintoma='miedo_especifico'),
        Fact(sintoma='timidez')
    ))
    def remedio_mimulus(self):
        self.declare(Fact(
            recomendacion="Mimulus",
            dosis="4 gotas, 3 veces al día",
            explicacion="Para miedos conocidos como hablar en público"
        ))

    @Rule(OR(
        Fact(sintoma='miedo_irracional'),
        Fact(sintoma='presentimientos')
    ))
    def remedio_aspen(self):
        self.declare(Fact(
            recomendacion="Aspen",
            dosis="3 gotas cada 4 horas",
            explicacion="Para temores vagos o desconocidos"
        ))

    @Rule(OR(
        Fact(sintoma='terror'),
        Fact(sintoma='panico')
    ))
    def remedio_rock_rose(self):
        self.declare(Fact(
            recomendacion="Rock Rose",
            dosis="2 gotas en emergencias",
            explicacion="Para situaciones de terror paralizante"
        ))

    @Rule(OR(
        Fact(sintoma='miedo_perder_control'),
        Fact(sintoma='impulsos_destructivos')
    ))
    def remedio_cherry_plum(self):
        self.declare(Fact(
            recomendacion="Cherry Plum",
            dosis="4 gotas cada 2 horas",
            explicacion="Para miedo a perder el control"
        ))

    @Rule(OR(
        Fact(sintoma='preocupacion_otros'),
        Fact(sintoma='miedo_por_seres_queridos')
    ))
    def remedio_red_chestnut(self):
        self.declare(Fact(
            recomendacion="Red Chestnut",
            dosis="3 gotas, 3 veces al día",
            explicacion="Para quienes sufren por sus seres queridos"
        ))

    @Rule(OR(
        Fact(sintoma='duda_constante'),
        Fact(sintoma='busca_aprobacion')
    ))
    def remedio_cerato(self):
        self.declare(Fact(
            recomendacion="Cerato",
            dosis="4 gotas antes de decisiones",
            explicacion="Para quienes dudan de sus decisiones"
        ))

    @Rule(OR(
        Fact(sintoma='indecision'),
        Fact(sintoma='oscilacion_emocional')
    ))
    def remedio_scleranthus(self):
        self.declare(Fact(
            recomendacion="Scleranthus",
            dosis="2 gotas cada hora",
            explicacion="Para dificultad al elegir"
        ))

    @Rule(OR(
        Fact(sintoma='desaliento'),
        Fact(sintoma='pesimismo')
    ))
    def remedio_gentian(self):
        self.declare(Fact(
            recomendacion="Gentian",
            dosis="3 gotas cada 3 horas",
            explicacion="Para el desánimo tras contratiempos"
        ))

    @Rule(OR(
        Fact(sintoma='desesperanza'),
        Fact(sintoma='derrotismo')
    ))
    def remedio_gorse(self):
        self.declare(Fact(
            recomendacion="Gorse",
            dosis="4 gotas cada 4 horas",
            explicacion="Para sentimientos de desesperanza"
        ))

    @Rule(OR(
        Fact(sintoma='fatiga_mental'),
        Fact(sintoma='postergacion')
    ))
    def remedio_hornbeam(self):
        self.declare(Fact(
            recomendacion="Hornbeam",
            dosis="3 gotas al despertar",
            explicacion="Para el cansancio mental"
        ))

    @Rule(OR(
        Fact(sintoma='incertidumbre_vocacional'),
        Fact(sintoma='insatisfaccion')
    ))
    def remedio_wild_oat(self):
        self.declare(Fact(
            recomendacion="Wild Oat",
            dosis="4 gotas, 2 veces al día",
            explicacion="Para incertidumbre sobre el camino de vida"
        ))

    @Rule(OR(
        Fact(sintoma='ensuenio_excesivo'),
        Fact(sintoma='desconexion_realidad')
    ))
    def remedio_clematis(self):
        self.declare(Fact(
            recomendacion="Clematis",
            dosis="3 gotas cada 3 horas",
            explicacion="Para falta de concentración"
        ))

    @Rule(OR(
        Fact(sintoma='nostalgia'),
        Fact(sintoma='apego_pasado')
    ))
    def remedio_honeysuckle(self):
        self.declare(Fact(
            recomendacion="Honeysuckle",
            dosis="4 gotas cuando surja el recuerdo",
            explicacion="Para vivir anclado en el pasado"
        ))

    @Rule(OR(
        Fact(sintoma='apatia'),
        Fact(sintoma='resignacion')
    ))
    def remedio_wild_rose(self):
        self.declare(Fact(
            recomendacion="Wild Rose",
            dosis="3 gotas cada 4 horas",
            explicacion="Para falta de motivación"
        ))

    @Rule(OR(
        Fact(sintoma='agotamiento_extremo'),
        Fact(sintoma='fatiga_fisica')
    ))
    def remedio_olive(self):
        self.declare(Fact(
            recomendacion="Olive",
            dosis="4 gotas cada 2 horas",
            explicacion="Para agotamiento físico y mental"
        ))

    @Rule(OR(
        Fact(sintoma='pensamientos_recurrentes'),
        Fact(sintoma='mente_ruidosa')
    ))
    def remedio_white_chestnut(self):
        self.declare(Fact(
            recomendacion="White Chestnut",
            dosis="3 gotas cuando aparezcan los pensamientos",
            explicacion="Para diálogo interno constante"
        ))

    @Rule(OR(
        Fact(sintoma='tristeza_sin_razon'),
        Fact(sintoma='melancolia')
    ))
    def remedio_mustard(self):
        self.declare(Fact(
            recomendacion="Mustard",
            dosis="4 gotas cuando aparezca la tristeza",
            explicacion="Para tristeza sin causa aparente"
        ))

    @Rule(OR(
        Fact(sintoma='repeticion_errores'),
        Fact(sintoma='dificultad_aprender')
    ))
    def remedio_chestnut_bud(self):
        self.declare(Fact(
            recomendacion="Chestnut Bud",
            dosis="3 gotas, 3 veces al día",
            explicacion="Para aprender de las experiencias"
        ))

    @Rule(OR(
        Fact(sintoma='shock'),
        Fact(sintoma='estres_agudo'),
        Fact(sintoma='emergencia_emocional')
    ))
    def remedio_rescue_remedy(self):
        self.declare(Fact(
            recomendacion="Rescue Remedy",
            dosis="4 gotas bajo la lengua",
            explicacion="Para situaciones de crisis emocional"
        ))

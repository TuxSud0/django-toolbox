from django.db import models
#from django.contrib.auth.models import User

PROJECT_NAME = 'Sulfur Reliability'
PROJECT_NUMBER_BASE = '07QY74'
PROJECT_SITE = 'Garyville, LA'
STATIC_DEF = {}
WBS_DEF = {
	"020": "COORDINATION",
	"050": "FIELD TRIPS",
	"060": "ESTIMATES",
	"120": "SQUAD CHECK",
	"300": "MECHANICAL SERVICES",
	"301": "PUMPS",
	"302": "COMPRESSORS",
	"303": "FANS & BLOWERS",
	"304": "CLARIFIERS and SETTLERS",
	"305": "AGITATORS AND MIXERS",
	"306": "FIRED EQUIPMENT",
	"307": "REFRIGERATION",
	"308": "LIFTING EQUIPMENT",
	"309": "ATMOSPHERIC VESSELS",
	"310": "WET SCRUBBERS",
	"311": "HEAT EXCHANGERS",
	"312": "COLUMNS and INTERNALS",
	"313": "PRESSURE VESSELS",
	"314": "REACTORS",
	"315": "STORAGE BINS",
	"316": "EVAPORATORS",
	"317": "STEAM GENERATORS",
	"318": "COOLING TOWERS",
	"319": "STACKS",
	"320": "EXTRUDERS",
	"321": "CENTRIFUGES",
	"322": "FILTERS & SILENCERS",
	"323": "CYCLONES",
	"324": "AIR POLLUTION CONTROL",
	"325": "DRYERS",
	"326": "CRUSHERS",
	"327": "GRINDERS",
	"328": "SCREENS",
	"329": "BELT AND ROLLER CONVEYORS",
	"330": "SCREW CONVEYORS",
	"331": "BUCKET ELEVATORS",
	"332": "PAN FEEDERS",
	"333": "VIBRATING FEEDERS",
	"334": "WEIGH SCALES",
	"335": "CHUTES",
	"336": "MISCELLANEOUS",
	"337": "PACKAGED UNITS",
	"338": "SPECIALTY VALVES",
	"339": "POWER TRANSMISSION",
	"340": "SEPARATORS",
	"341": "COALESCERS",
	"342": "AIR COOLED EXCHANGERS",
	"343": "HVAC SYSTEMS",
	"344": "FIRE PROTECTION",
	"345": "SPECIALTY ITEMS",
	"346": "PIPING COMPONENTS",
	"347": "STRUCTURAL COMPONENTS",
	"348": "PAINT, INSULATION, FIREPROOFING,REFRACTORY",
	"349": "CHEMICALS AND LUBRICANTS",
	"350": "PIPING BY MECHANICAL",
	"360": "CIVIL / STRUCTURAL BY MECHANICAL",
	"370": "ELECTRICAL BY MECHANICAL",
	"380": "CONTROLS BY MECHANICAL",
	"390": "CONSTRUCTION BY MECHANICAL"
	}

class Definition(models.Model):
	wbs_keys=list(WBS_DEF.keys())
	wbs_d = {}
	i = 0
	while i < len(wbs_keys):
		wbs_d[wbs_keys[i]]= str(wbs_keys[i]) #+ " - " + str(WBS_DEF.get(wbs_keys[i]))
		i+=1
	wbs_choices = list(wbs_d.items())
	
	E = 'Heat Exchanger'
	G = 'Pump'
	D = 'Vessel'
	EJ = 'Ejector'
	MISC = 'MISC'
	eq_class_choices = [
		('E',E),
		('G',G),
		('D',D),
		('EJ',EJ)
	]
	bat_lim_choices = [('ISBL','ISBL'),('OSBL','OSBL')]
	tag = models.CharField(primary_key=True, max_length=20)
	desc = models.CharField(max_length=50, blank=True, null=True)
	wbs = models.CharField(choices=wbs_choices,max_length=5)
	pkg = models.CharField(max_length=50, blank=True, null=True)
	est_group = models.CharField(max_length=50, blank=True, null=True)
	bat_lim = models.CharField(choices=bat_lim_choices,max_length=5, null=True)
	pid = models.CharField(max_length=50, blank=True, null=True)
	pfd = models.CharField(max_length=50, blank=True, null=True)
	eq_class = models.CharField(choices=eq_class_choices, max_length=20,null=True)
	#wbs2 = models.ForeignKey(
	#	'Wbs',
	#	on_delete=
	#)
#	),on_delete=models.SET_NULL,null=True)
	#packages=models.QuerySet(model='Package',query='select number')
	def __str__(self):
		return str(self.tag)

class Package(models.Model):
	auto_id = models.AutoField(primary_key=True)
	number = models.CharField(unique=True, max_length=20)
	name = models.CharField(max_length=30, blank=True, null=True)

	def __str__(self):
		return str(self.number)

class Wbs(models.Model):
    code = models.CharField(max_length=5,primary_key=True)
    description = models.CharField(max_length=50)
    equipment_type = models.CharField(max_length=20,null=True)

    def __str__(self):
        return str(self.code)

class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.type)

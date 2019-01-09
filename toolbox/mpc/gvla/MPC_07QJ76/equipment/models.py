from django.db import models
#from django.contrib.auth.models import User

PROJECT_NAME = 'Sulfur Reliability'
PROJECT_NUMBER_BASE = '07OT89'
PROJECT_SITE = 'Garyville, LA'
STATIC_DEF = {}
WBS_CODES = [
	('020','020'),
	('050','050'),
        ('060','060'),
        ('120','120'),
        ('300','300'),
        ('301','301'),
        ('302','302'),
        ('303','303'),
        ('306','306'),
        ('311','311'),
        ('312','312'),
        ('313','313'),
	]

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
	auto_id = models.AutoField(primary_key=True)
	tag = models.CharField(unique=True, max_length=20)
	name = models.CharField(max_length=20, blank=True, null=True)
	wbs = models.CharField(choices=WBS_CODES,max_length=5)
	#_type = models.ForeignKey('resource.Wbs',on_delete=models.SET_NULL,null=True,default="")
	
	def __str__(self):
		return str(self.tag)

class Package(models.Model):
	auto_id = models.AutoField(primary_key=True)
	number = models.CharField(unique=True, max_length=20)
	name = models.CharField(max_length=30, blank=True, null=True)

	def __str__(self):
		return str(self.number)

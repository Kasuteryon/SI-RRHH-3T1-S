from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Adelantosalario),
admin.site.site_header = "Administrador SIRRHH"
admin.site.site_title = "Administrar"
admin.site.index_title = "Bienvenido al Panel de Administración"

admin.site.register(Areaempresa),
admin.site.register(Bitacora),
#admin.site.register(Campoinstrumento),
admin.site.register(Cargo),
#admin.site.register(Cargosalario),
#admin.site.register(Casadeestudio),
# admin.site.register(CatFechasession),
admin.site.register(CatFunciones),
admin.site.register(CatHabilidades),
admin.site.register(CatPadecimientos),
admin.site.register(CatPublicidad),
admin.site.register(CatRedessociales),
admin.site.register(CatRequerimientos),
admin.site.register(CatRols),
#admin.site.register(CatTipoestudio),
admin.site.register(CatTipopadecimiento),
admin.site.register(CatTipovacante),
admin.site.register(Catciudad),
admin.site.register(Catprueba),
admin.site.register(Companiatelefonica),
# admin.site.register(Conexiones),
# admin.site.register(Contrato),
#admin.site.register(Correopersona),
#admin.site.register(Dependientes),
#admin.site.register(Descripcionparentesco),
#admin.site.register(DetNomina),
admin.site.register(Detalletablaprogresiva),
#admin.site.register(Direccionpersona),
#admin.site.register(Empleado),
#admin.site.register(Empleadoformato),
#admin.site.register(Empleadoprueba),
#admin.site.register(Entradasalidas),
#admin.site.register(Entrevista1),
#admin.site.register(Entrevista2),
admin.site.register(Estadocivil),
#admin.site.register(Estadopostulante),
#admin.site.register(Estudiopersona),
admin.site.register(Examenes),
#admin.site.register(Examenpostulante),
admin.site.register(Formatoprueba),
admin.site.register(Funcionescargo),
admin.site.register(Habilidadesempleados),
#admin.site.register(Historialcargo),
#admin.site.register(Historiallaboral),
admin.site.register(Horariolaboral),
#admin.site.register(Horasextra),
admin.site.register(Idiomas),
admin.site.register(Incentivos),
admin.site.register(Instrumento),
#admin.site.register(Intentossession),
admin.site.register(Licencia),
#admin.site.register(Llegadastardias),
#admin.site.register(Nomina),
#admin.site.register(Numtelefono),
#admin.site.register(Paginaweb),
admin.site.register(Paisorigen),
admin.site.register(Parentesco),
admin.site.register(Periodolaboral),
#admin.site.register(Permisos),
#admin.site.register(Permisossecurity),
admin.site.register(Persona),
#admin.site.register(Personaidioma),
#admin.site.register(Personaredsocial),
#admin.site.register(Postulantes),
admin.site.register(Proveedorservicios),
#admin.site.register(Referencias),
#admin.site.register(Representacionlegal),
admin.site.register(Requisitoscargo),
#admin.site.register(Revisionoficial),
#admin.site.register(Revisionpreliminar),
#admin.site.register(Rolusuario),
admin.site.register(Tablaprogresiva),
admin.site.register(Tipocontrato),
admin.site.register(Tipofuncion),
admin.site.register(Tipoincentivo),
admin.site.register(Tiporequisito),
admin.site.register(Tipovacacion),
admin.site.register(Titulos),
admin.site.register(Usuarioempleado),
admin.site.register(Usuariopostulante),
#admin.site.register(Vacacioneacumuladas),
admin.site.register(Vacante),


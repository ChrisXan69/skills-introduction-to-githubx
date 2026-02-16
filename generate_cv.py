from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.units import cm

# --- Configuración del Documento ---
filename = "CV_Christopher_Mendoza_Sanchez_Redesign.pdf"
doc = SimpleDocTemplate(filename, pagesize=A4,
                        rightMargin=1.5*cm, leftMargin=1.5*cm,
                        topMargin=1.5*cm, bottomMargin=1.5*cm)

styles = getSampleStyleSheet()

# --- Definición de Colores ---
COLOR_PRIMARY = colors.HexColor("#1B3A57")  # Azul Marino Elegante
COLOR_ACCENT = colors.HexColor("#476C9B")   # Azul Acero para subtítulos
COLOR_TEXT = colors.HexColor("#2C3E50")     # Gris oscuro para texto
COLOR_BG_SIDEBAR = colors.HexColor("#F4F6F7") # Gris muy tenue para fondo (opcional visual)

# --- Estilos Personalizados ---
# Nombre Principal
style_name = ParagraphStyle(
    'Name',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=22,
    textColor=COLOR_PRIMARY,
    alignment=TA_LEFT,
    spaceAfter=2
)

# Título Profesional
style_title = ParagraphStyle(
    'Title',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=11,
    textColor=COLOR_ACCENT,
    alignment=TA_LEFT,
    spaceAfter=15
)

# Títulos de Sección (Experiencia, Educación, etc.)
style_heading = ParagraphStyle(
    'SectionHeading',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=12,
    textColor=COLOR_PRIMARY,
    spaceBefore=10,
    spaceAfter=6,
    borderPadding=0
)

# Títulos de Trabajos/Puestos
style_job_title = ParagraphStyle(
    'JobTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    textColor=colors.black,
    spaceAfter=1
)

# Empresa y Fecha
style_job_details = ParagraphStyle(
    'JobDetails',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9,
    textColor=colors.grey,
    spaceAfter=4
)

# Cuerpo de texto (Bullets)
style_body = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=11,
    textColor=COLOR_TEXT,
    alignment=TA_JUSTIFY
)

# Texto pequeño para sidebar
style_sidebar_text = ParagraphStyle(
    'Sidebar',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=10,
    textColor=COLOR_TEXT,
    spaceAfter=4
)

style_sidebar_header = ParagraphStyle(
    'SidebarHeader',
    parent=styles['Heading3'],
    fontName='Helvetica-Bold',
    fontSize=10,
    textColor=COLOR_PRIMARY,
    spaceBefore=8,
    spaceAfter=4
)

# --- Contenido ---

# 1. Header (Nombre y Datos de Contacto en una línea debajo si se desea, o en sidebar)
header_content = []
header_content.append(Paragraph("CHRISTOPHER MENDOZA SÁNCHEZ", style_name))
header_content.append(Paragraph("Profesional Técnico en Administración | Especialista en Optimización de Procesos &amp; IA", style_title))
header_content.append(HRFlowable(width="100%", thickness=1, color=COLOR_ACCENT, spaceAfter=10))

# 2. Definición de Columnas
# Columna Izquierda (Sidebar): 30% ancho - Datos, Skills, Educación
# Columna Derecha (Main): 70% ancho - Perfil, Experiencia, Proyectos

# --- Contenido Columna Izquierda ---
sidebar_content = []

# Contacto
sidebar_content.append(Paragraph("CONTACTO", style_sidebar_header))
sidebar_content.append(Paragraph("📍 Tepic, Nayarit", style_sidebar_text))
sidebar_content.append(Paragraph("📱 311 260 5519", style_sidebar_text))
sidebar_content.append(Paragraph("📧 cms050104@gmail.com", style_sidebar_text))

# Educación
sidebar_content.append(Paragraph("EDUCACIÓN", style_sidebar_header))
sidebar_content.append(Paragraph("<b>Licenciatura en Psicología</b><br/>(Nivel Avanzado - 8.º Semestre)<br/>Univ. Autónoma de Nayarit", style_sidebar_text))
sidebar_content.append(Paragraph("<i>Enfoque: Psicología Organizacional</i>", style_sidebar_text))
sidebar_content.append(Spacer(1, 6))
sidebar_content.append(Paragraph("<b>Prof. Téc. en Administración</b><br/>CONALEP Tepic<br/><i>Modelo Dual Auxiliar Contable</i>", style_sidebar_text))

# Competencias Técnicas (Software)
sidebar_content.append(Paragraph("SOFTWARE &amp; ERP", style_sidebar_header))
sidebar_content.append(Paragraph("• SAP (Módulos Admin)", style_sidebar_text))
sidebar_content.append(Paragraph("• Contpaq (Nómina, Bancos)", style_sidebar_text))
sidebar_content.append(Paragraph("• Excel Avanzado (Macros)", style_sidebar_text))
sidebar_content.append(Paragraph("• CFDI 4.0 / Facturación", style_sidebar_text))

# Innovación e IA (Highlight)
sidebar_content.append(Paragraph("TECNOLOGÍA &amp; IA", style_sidebar_header))
sidebar_content.append(Paragraph("• Ingeniería de Prompts", style_sidebar_text))
sidebar_content.append(Paragraph("• Agentes GPT Personalizados", style_sidebar_text))
sidebar_content.append(Paragraph("• Análisis Big Data", style_sidebar_text))
sidebar_content.append(Paragraph("• Automatización de Workflows", style_sidebar_text))

# Habilidades Blandas
sidebar_content.append(Paragraph("SKILLS DIRECTIVOS", style_sidebar_header))
sidebar_content.append(Paragraph("• Liderazgo de Equipos", style_sidebar_text))
sidebar_content.append(Paragraph("• Negociación Estratégica", style_sidebar_text))
sidebar_content.append(Paragraph("• Resolución de Conflictos", style_sidebar_text))
sidebar_content.append(Paragraph("• Auditoría Interna", style_sidebar_text))

# --- Contenido Columna Derecha ---
main_content = []

# Perfil (Resumido y potente)
main_content.append(Paragraph("PERFIL PROFESIONAL", style_heading))
main_content.append(Paragraph(
    "Administrador proactivo con sólida trayectoria en gestión integral y operaciones comerciales. "
    "Especialista en la transformación digital de procesos tradicionales mediante Inteligencia Artificial y análisis de datos. "
    "Poseo una visión estratégica única que combina el rigor administrativo (SAP, KPIs, Finanzas) con la psicología organizacional, "
    "permitiéndome liderar equipos de alto rendimiento y maximizar la rentabilidad operativa.",
    style_body
))

# Experiencia Profesional
main_content.append(Paragraph("EXPERIENCIA PROFESIONAL", style_heading))

# Job 1
main_content.append(Paragraph("ENCARGADO Y ADMINISTRADOR DE SUCURSAL", style_job_title))
main_content.append(Paragraph("Minisuper &amp; Depósito Antonella | Marzo 2024 – Enero 2025", style_job_details))
main_content.append(Paragraph(
    "• <b>Reingeniería Comercial:</b> Ejecuté reestructuración de precios y layout, logrando incremento medible en margen de utilidad.<br/>"
    "• <b>Optimización de Inventarios:</b> Implementé 'Stock Crítico', reduciendo mermas y costos operativos.<br/>"
    "• <b>Customer Success:</b> Implanté protocolos de atención recuperando cuentas clave y fidelizando clientes.<br/>"
    "• <b>Gestión de Talento:</b> Capacitación operativa enfocada en eficiencia y ventas cruzadas.",
    style_body
))
main_content.append(Spacer(1, 6))

# Job 2
main_content.append(Paragraph("ADMINISTRADOR GENERAL", style_job_title))
main_content.append(Paragraph("Carpintería y Diseño Tepic | Febrero 2023 – Enero 2024", style_job_details))
main_content.append(Paragraph(
    "• <b>Control Financiero:</b> Responsable total del flujo de caja (Cash Flow), presupuestos y supervisión de inventarios.<br/>"
    "• <b>Transformación Digital:</b> Profesionalización de imagen y gestión de redes sociales, expandiendo la cartera de clientes.<br/>"
    "• <b>Gestión de Proyectos:</b> Planificación basada en objetivos, mejorando tiempos de entrega y productividad del taller.<br/>"
    "• <b>Mediación:</b> Aplicación de psicología organizacional para resolución de conflictos y clima laboral.",
    style_body
))
main_content.append(Spacer(1, 6))

# Job 3
main_content.append(Paragraph("AUXILIAR ADMINISTRATIVO, CONTABLE Y LOGÍSTICA", style_job_title))
main_content.append(Paragraph("Edificaciones Estructuras Ex Marín / Bigeyes | Enero 2020 – Dic 2022", style_job_details))
main_content.append(Paragraph(
    "• <b>Soporte ERP:</b> Manejo experto de SAP y Contpaq (Conciliaciones, Nómina, Facturación).<br/>"
    "• <b>Sistematización:</b> Diseño de sistema en Excel para control de almacén, eliminando errores humanos.<br/>"
    "• <b>Logística y Compras:</b> Negociación con proveedores estratégicos y logística de materiales de construcción.<br/>"
    "• <b>Compliance:</b> Organización fiscal para auditorías internas y cumplimiento SAT.",
    style_body
))

# Proyectos Destacados (Esta sección es clave para tu perfil de IA)
main_content.append(Paragraph("PROYECTO DESTACADO: INNOVACIÓN Y TECNOLOGÍA", style_heading))
main_content.append(Paragraph("DESARROLLO DE SISTEMA ERP CON INTELIGENCIA ARTIFICIAL", style_job_title))
main_content.append(Paragraph("Negocio Familiar (Sector Retail/Florería)", style_job_details))
main_content.append(Paragraph(
    "Lideré la arquitectura de negocio y transformación digital completa:<br/>"
    "• <b>IA &amp; Chatbots:</b> Diseño de portal en la nube con Agentes IA. Chatbot de ventas para cierre/leads y módulos automatizados de inventarios/finanzas.<br/>"
    "• <b>Business Intelligence:</b> Generación de dashboards en tiempo real para toma de decisiones estratégicas.",
    style_body
))

# --- Ensamblaje de la Tabla Principal ---
# Convertir listas de flowables en una sola celda para la tabla
sidebar_flowables = sidebar_content
main_flowables = main_content

# Estructura de tabla: [Columna Izq, Columna Der]
data = [[sidebar_flowables, main_flowables]]

# Anchos de columna: Sidebar 5.5cm, Main 12cm aprox
table = Table(data, colWidths=[5.5*cm, 12.5*cm])

# Estilo de la tabla (Alineación superior, padding, línea divisoria vertical)
table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 0),
    ('LINEAFTER', (0,0), (0,-1), 0.5, colors.lightgrey), # Línea vertical divisoria
]))

story = []
story.extend(header_content)
story.append(Spacer(1, 10))
story.append(table)

# Generar PDF
doc.build(story)

print(f"PDF generado exitosamente: {filename}")

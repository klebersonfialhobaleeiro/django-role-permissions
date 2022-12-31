from rolepermissions.roles import AbstractUserRole

class Secretaria(AbstractUserRole):
    available_permissions = {
        'cadastrar_medico': True,
        'cadastrar_secretaria': True,
    }

class Medico(AbstractUserRole):
    available_permissions = {
        'enviar_atestado': True,
        'enviar_receita': True,
    }

class Paciente(AbstractUserRole):
    available_permissions = {
        'agendar_consulta': True,
        'cadastrar_paciente': True,
        'atualizar_paciente': True,
    }
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class employee(models.Model):
    _name = 'agromes.employee'

    surname = fields.Char()
    name = fields.Char()
    patronymic = fields.Char()
    archive = fields.Boolean()
    department = fields.Char()
    specialty = fields.Char()
    telephone = fields.Char()
    email = fields.Char()
    rfid = fields.Char()
    description = fields.Char()
    code = fields.Char()

	
class machines (models.Model):
    _name = 'agromes.machines'

    title = fields.Char()
    platenumber = fields.Char()
    archive = fields.Char()
    ishired = fields.Boolean()
    department = fields.Char()
    model = fields.Char()
    machinetype = fields.Char()
    isindependent = fields.Boolean()
    manufactured = fields.Integer()
    code = fields.Char()
    color = fields.Integer()
    description = fields.Char()
	
class settingmachines (models.Model):
    _name = 'agromes.settingmachines'

    typesTE = fields.Char()
    workingwidth = fields.Float()
    workingdepth = fields.Float()
    volumebarrel = fields.Float()
    power = fields.Float()
    productivity = fields.Float()
    consumptiongsm = fields.Float()
    telematicsprovider = fields.Char()
    monitoringcode = fields.Char()
    anchoreddriver = fields.Char()
    rfid = fields.Char()
	
class general_information (models.Model):
    _name = 'agromes.general_information'

    name = fields.Char()
    colour = fields.Integer()
    IIN = fields.Integer()
    address = fields.Char()
    name_director = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    note = fields.Text()

class settingg (models.Model):
    _name = 'agromes.settingg'
    reference_work_type = fields.Char()
    plan_actual = fields.Char()
    time_zone = fields.Char()

class structure_company (models.Model):
    _name = 'agromes.structure_company'

    name = fields.Char()
    typ = fields.Char()
    IIN = fields.Integer()
    address = fields.Char()
    name_director = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    notation = fields.Char()
    cipher = fields.Char()

class technologies_of_cultivation (models.Model):
    _name = 'agromes.technologies_of_cultivation'


    technology = fields.Char()
    archive = fields.Boolean()
    abbreviation = fields.Char()
    culture = fields.Char()
    ready_to_use = fields.Integer()

class import_tcult  (models.Model):
    _name = 'agromes.import_tcult'

    technology = fields.Char()
    abbreviation = fields.Char()
    culture = fields.Char()

class add_tcult (models.Model):
    _name = 'agromes.add_tcult'

    technology = fields.Char()
    archive = fields.Boolean()
    abbreviation = fields.Char()
    culture = fields.Char()
    planned_productivity_ centner_hectare = fields.Integer()
    notes = fields.Char()
    ready_to_use = fields.Char()

class barley_tcult (models.Model):
    _name = 'agromes.barley_tcult'

    name_technology = fields.Char()
    archive = fields.Boolean()
    abbreviation = fields.Char()
    culture = fields.Char()
    planned_productivity_centner_hectare = fields.Integer()
    ready_to_use = fields.Char()
    notes = fields.Char()



class application_technology (models.Model):
    _name = 'agromes.application_technology '

    season=fields.Char()
    number_of_fields=fields.Integer()
    area_hectares=fields.Integer()
    total=fields.Integer()

class  event(models.Model):
 _name = 'agromes.event'

    id=fields.Char()
    event=fields.Char()
    all_kinds_of_work_all_types_of_work=fields.Char()
    check_list=fields.Char()
    beginning_of_work=fields.Integer()
    number_of_days=fields.Integer()

	
	

		
# class anar1(models.Model):
    # _name = 'katu5.anar1'

    # name = fields.Char()
    # value4 = fields.Integer()


# class anar2(models.Model):
    # _name = 'katu5.anar2'

    # name = fields.Char()
    # value2 = fields.Integer()
	
# class anar3(models.Model):
    # _name = 'katu5.anar3'

    # name = fields.Char()
    # value5 = fields.Integer()
	

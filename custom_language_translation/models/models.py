# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from dateutil import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.osv import expression

import logging

_logger = logging.getLogger(__name__)




# please first run this command on your system in order to work with translation
# pip install googletrans==3.1.0a0


try:
	from googletrans import Translator
except ImportError:
	raise ImportError(
		'This module needs googletrans to automatically translate texts. '
		'Please install googletrans on your system. ( sudo pip install googletrans==3.1.0a0 )')



class warehouse_inherit(models.Model):
	_inherit = "stock.picking.type"



	name_translated = fields.Char(string='Translated Name')


	def _compute_picking_count(self):
		res = super(warehouse_inherit, self)._compute_picking_count()


		for data in self:

			if data.name:

				 # using googletranslate to translate the name 

				try:
					translator = Translator()
					translate_text = translator.translate(data.name,dest='ar',src='auto').text

					# translating to arabic language
					
					data.name_translated = translate_text

				except:
					ValidationError('Network is Slow, Please Fix Your Network Now!')

			else:
				pass


		return res
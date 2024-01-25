import odoorpc

odoo = odoorpc.ODOO('localhost', port=8069)

# Login
odoo.login('lacos', 'admin', 'admin')

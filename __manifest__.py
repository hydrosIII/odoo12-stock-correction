# Copyright 2020 Anvar Kildebekov <https://it-projects.info/team/fedoranvar>
# License MIT (https://opensource.org/licenses/MIT).

{
    "name": """Reset stock.quant""",
    "summary": """Clears and fills stock.quant with stock.move.lines incomes and outcomes""",
    "category": "Sales",
    # "live_test_url": "http://apps.it-projects.info/shop/product/DEMO-URL?version=12.0",
    "images": [],
    "version": "12.0.1.0.1",
    "application": False,

    "author": "IT-Projects LLC, Anvar Kildebekov",
    "support": "apps@it-projects.info",
    "website": "https://apps.odoo.com/apps/modules/12.0/stock_balance/",
    "license": "Other OSI approved licence",  # MIT
    # "price": 9.00,
    # "currency": "EUR",

    "depends": [
        'stock',
        'sale'
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'data/cron_balance.xml',
        'security/ir.model.access.csv'
    ],
    "demo": [
    ],
    "qweb": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,

    # "demo_title": "Income-Outcome to Stock Quant",
    # "demo_addons": [
    # ],
    # "demo_addons_hidden": [
    # ],
    # "demo_url": "DEMO-URL",
    # "demo_summary": "Put Income-Outcome to Stock.Quant",
    # "demo_images": [
    #    "images/MAIN_IMAGE",
    # ]
}

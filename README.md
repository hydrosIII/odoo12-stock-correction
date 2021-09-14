# odoo12-stock-correction
Odoo module that works with stock correction. It is intendend to run monthly or weekly. Depending on the server hardware it can take as long as 12 hours to run.

This is an odoo module to correct an error in odoo 12 to use when in the table stock_qty the qty is wrong and do not check with the sum od the stock movements. So we have to recalculate the stock from the stock_moves. This script sums all the stock moves and then writes the sum directly to the stock_qty table. It can take a long time to run, so it is better to leave it running during night, or weekends. It can be installed as a module an it provides an automatic and periodic task that can be configured in odoo under server actions.

This script is thought to be used with odoo-stock-correct-short from my other repo https://github.com/hydrosIII/odoo12-stock-correction-short, The short script is thought too run daily.

The original author of this script it ittplabs https://github.com/itpp-labs, but it was written on my comission.

GPL v2 license.


import ecommerce.shipping
from ecommerce.shipping import calc_shipping
# This is how to import the entire module without having to specify the function
from ecommerce import shipping

ecommerce.shipping.calc_shipping()

calc_shipping()

# now we can use all functions without the package prefix
shipping.calc_tax()
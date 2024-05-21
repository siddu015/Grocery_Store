import pydot

# Create a graph object
graph = pydot.Dot(graph_type='digraph')

# Define nodes for each table
products_node = pydot.Node('Products', shape='record', label='Products|{product_id: INT|name: VARCHAR(255)|price_per_unit: DECIMAL(10,2)|uom_id: INT}')
uom_node = pydot.Node('Uom', shape='record', label='Uom|{uom_id: INT|uom_name: VARCHAR(45)}')
customers_node = pydot.Node('Customers', shape='record', label='Customers|{customer_id: INT|customer_name: VARCHAR(255)|email: VARCHAR(255)|phone: VARCHAR(20)|address: TEXT}')
orders_node = pydot.Node('Orders', shape='record', label='Orders|{order_id: INT|customer_id: INT|datetime: DATETIME|total: DECIMAL(10,2)}')
order_details_node = pydot.Node('Order_Details', shape='record', label='Order_Details|{order_id: INT|product_id: INT|quantity: INT|total_price: DECIMAL(10,2)}')

# Add nodes to the graph
graph.add_node(products_node)
graph.add_node(uom_node)
graph.add_node(customers_node)
graph.add_node(orders_node)
graph.add_node(order_details_node)

# Define edges for foreign key relationships
graph.add_edge(pydot.Edge('Products', 'Uom', label='uom_id', arrowhead='none'))
graph.add_edge(pydot.Edge('Orders', 'Customers', label='customer_id', arrowhead='none'))
graph.add_edge(pydot.Edge('Order_Details', 'Orders', label='order_id', arrowhead='none'))
graph.add_edge(pydot.Edge('Order_Details', 'Products', label='product_id', arrowhead='none'))

# Save the graph to a file
graph.write_png('er_diagram.png')

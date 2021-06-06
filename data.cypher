LOAD CSV WITH HEADERS  FROM "file:///stock.csv" AS line MERGE (s:stock{stock_code:line.stock_code,name:line.stock});

LOAD CSV WITH HEADERS  FROM "file:///latest_price.csv" AS line MERGE (a:latest_price{id:line.latest_price,value:line.value});
LOAD CSV FROM "file:///a.csv" AS line MATCH (from:stock{stock_code:line[0]}) MATCH (to:latest_price{id:line[1]}) merge (from)-[r:of]-> (to);

LOAD CSV WITH HEADERS  FROM "file:///quote_change.csv" AS line MERGE (b:quote_change{id:line.quote_change,value:line.value});
LOAD CSV FROM "file:///b.csv" AS line MATCH (from:stock{stock_code:line[0]}) MATCH (to:quote_change{id:line[1]}) merge (from)-[r:of]-> (to);

LOAD CSV WITH HEADERS  FROM "file:///PE_TTM.csv" AS line MERGE (c:PE_TTM{id:line.PE_TTM,value:line.value});
LOAD CSV FROM "file:///c.csv" AS line MATCH (from:stock{stock_code:line[0]}) MATCH (to:PE_TTM{id:line[1]}) merge (from)-[r:of]-> (to);

LOAD CSV WITH HEADERS  FROM "file:///PE_static.csv" AS line MERGE (d:PE_static{id:line.PE_static,value:line.value});
LOAD CSV FROM "file:///d.csv" AS line MATCH (from:stock{stock_code:line[0]}) MATCH (to:PE_static{id:line[1]}) merge (from)-[r:of]-> (to);

LOAD CSV WITH HEADERS  FROM "file:///PB_ratio.csv" AS line MERGE (e:PB_ratio{id:line.PB_ratio,value:line.value});
LOAD CSV FROM "file:///e.csv" AS line MATCH (from:stock{stock_code:line[0]}) MATCH (to:PB_ratio{id:line[1]}) merge (from)-[r:of]-> (to);

LOAD CSV WITH HEADERS  FROM "file:///PEG.csv" AS line MERGE (f:PEG{id:line.PEG,value:line.value});
LOAD CSV FROM "file:///f.csv" AS line MATCH (from:stock{stock_code:line[0]}) MATCH (to:PEG{id:line[1]}) merge (from)-[r:of]-> (to);

LOAD CSV WITH HEADERS  FROM "file:///market_sales_rate.csv" AS line MERGE (g:market_sales_rate{id:line.market_sales_rate,value:line.value});
LOAD CSV FROM "file:///g.csv" AS line MATCH (from:stock{stock_code:line[0]}) MATCH (to:market_sales_rate{id:line[1]}) merge (from)-[r:of]-> (to);

LOAD CSV WITH HEADERS  FROM "file:///price_cash_rate.csv" AS line MERGE (h:price_cash_rate{id:line.price_cash_rate,value:line.value});
LOAD CSV FROM "file:///h.csv" AS line MATCH (from:stock{stock_code:line[0]}) MATCH (to:price_cash_rate{id:line[1]}) merge (from)-[r:of]-> (to);

LOAD CSV WITH HEADERS  FROM "file:///industry.csv" AS line MERGE (L:industry{id:line.industry,name:line.name});
LOAD CSV FROM "file:///L.csv" AS line MATCH (from:stock{stock_code:line[0]}) MATCH (to:industry{id:line[1]}) merge (from)-[r:belong]-> (to);
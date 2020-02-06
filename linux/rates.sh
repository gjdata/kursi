curl -s https://api.exchangeratesapi.io/latest | json2csv --flatten > rates
fields=`cat rates | head -n 1 | sed 's/rates//g' | tr -d '".'`
values=`cat rates | tail -n 1 | tr \" \'`
insert="INSERT INTO rates ($fields) VALUES ($values)"
result=`sudo mysql -u root --database test --execute "$insert"`
rm rates 

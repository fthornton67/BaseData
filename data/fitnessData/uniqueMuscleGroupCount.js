conn = new Mongo();
db = conn.getDB("mean-dev");
res = db.phitr_exercises.aggregate([
	{   $match: { } },
	{	$group:  { _id:"$muscleGroups",count: { $sum: 1 } } }
	
	]);
while (res.hasNext()) {
	printjson(res.next());
}

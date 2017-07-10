conn = new Mongo();
db = conn.getDB("phitrme-dev");
res = db.phitr_exercises.aggregate(  [ 
    { $unwind : "$muscleGroups" }, 
    { $group : { _id : "$muscleGroups", number : { $sum : 1 } } },
    { $sort : { number : -1 } },
  	{ $project : {_id: 0,groupName: '$_id' }}]);
while (res.hasNext()) {
	printjson(res.next());
}   
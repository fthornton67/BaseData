conn = new Mongo();
db = conn.getDB("mean-dev");
res = db.phitr_airports.find({
	loc: {
		$near: {
			$geometry: {
				"type": "Point",
				"coordinates": [ -122.309306, 47.449 ] 
			},
			$maxDistance: 5000
		}
	}
});
while (res.hasNext()) {
	printjson(res.next());
}

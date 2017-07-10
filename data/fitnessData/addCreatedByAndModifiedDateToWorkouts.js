conn = new Mongo();
db = conn.getDB("phitrme-dev");
res = db.phitr_workouts.update({createdBy:{$exists:true}},{$set: {'createdBy':ObjectId("540e565070f071000020f080"),'created':new Date(),'modified': new Date() }},{multi:true});

conn = new Mongo();
db = conn.getDB("phitrme-dev");

var muscleGroups ={};
db.phitr_muscle_groups.find({}).forEach(function(muscleGroup){
	muscleGroups[muscleGroup.groupName] = muscleGroup._id;  
	print(muscleGroup._id);
});
res = db.phitr_exercises.find({}).forEach(function(item) {                        
	if (item.muscleGroups !== undefined) {
		for (var i = 0; i < item.muscleGroups.length; i++) { 
			print(item.muscleGroups[i]); 
			item.muscleGroups[i] = muscleGroups[item.muscleGroups[i]]; 
			print(item.muscleGroups[i]);
		} 
	}  
	 	db.phitr_exercises.save(item);
	
});

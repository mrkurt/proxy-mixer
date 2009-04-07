Mixer = function(src){
	if(this.mode == "client"){
		document.writeln(src);
	}else{
		document.writeln("no!");
	}
};

Mixer.mode = "client";

document.writeln(Mixer.mode);
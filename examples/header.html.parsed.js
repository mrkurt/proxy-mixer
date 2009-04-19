var window = {};
if(window.MixerOptions == undefined){
	MixerOptions = {};
	MixerOptions.mode = 'server';
	MixerOptions.mode.error_messages = {};
}

if(window.Mixer == undefined){
	Mixer = function(src, options){
		if(Mixer.options == undefined || Mixer.options.mode == undefined || Mixer.options.mode == 'client'){
			var result = Mixer.client_include(src);
			
			if(result !== true){
				var errors = Mixer.options.error_messages;
				if(options != undefined && options.errors != undefined){
					if(result.status == 404 && options.errors.not_found != undefined){
						document.write(options.errors.not_found);
					}else if(options.errors.generic != undefined){
						document.write(options.errors.generic);
					}else{
						document.write("Unable to process include, no error specified");
					}
				}
			}
		}else{
			Mixer.output.push({'type' : 'include', 'src' : src, 'options' : options});
		}
	};
	
	Mixer.output = [];
	
	Mixer.client_include = function(src){
		s = Mixer.options.proxy == undefined ? src : Mixer.options.proxy + src;
		
		var req = new XMLHttpRequest();
		req.open('GET', s, false);
		req.send(null);
		console.debug(req.readyState);
		if(req.status == 200){
			document.write(req.responseText);
			return true;
		}else{
			return { status : req.status, success : false, url : src};
		}
	};
	
	Mixer.append_raw_from_array = function(index){
		Mixer.output.push({'type': 'raw', 'index' : index})
	}
	
	Mixer.options = MixerOptions == undefined ? {} : MixerOptions;
}
Mixer.append_raw_from_array(0);

Mixer.output;
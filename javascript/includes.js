if(window.MixerOptions == undefined){
  MixerOptions = {};
  MixerOptions.mode = 'client';
  MixerOptions.mode.error_messages = {};
}

if(window.Mixer == undefined){
  Mixer = function(src, options){
    if(Mixer.options == undefined || Mixer.options.mode == undefined || Mixer.options.mode == 'client'){
      var result = Mixer.client_include(src);
      
      if(result !== true){
      	if(options != undefined && options.errors != undefined){
      		if(result.status == 404 && options.errors.not_found != undefined){
      			document.writeln(options.errors.not_found);
      		}else if(options.errors.default != undefined){
      			document.writeln(options.errors.default);
      		}else{
      			document.writeln("Unable to process include, no error specified");
      		}
      	}
      }
    }else{
      document.writeln('Server side!: ' + src);
    }
  };
  
  Mixer.client_include = function(src){
    s = Mixer.options.proxy == undefined ? src : Mixer.options.proxy + src;
    
    var req = new XMLHttpRequest();
    req.open('GET', s, false);
    console.debug(req);
    req.send(null);
    if(req.status == 200){
      document.writeln(req.responseText);
      return true;
    }else{
      return { status : req.status, success : false, url : src};
    }
  };
  
  Mixer.options = MixerOptions == undefined ? {} : MixerOptions;
}
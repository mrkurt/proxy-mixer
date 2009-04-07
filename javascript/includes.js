if(window.MixerOptions == undefined){
  MixerOptions = {};
  MixerOptions.mode = 'client';
}

if(window.Mixer == undefined){
  Mixer = function(src){
    if(Mixer.is_client_side()){
      return Mixer.client_include(src);
    }else{
      document.writeln('Server side!: ' + src);
    }
  };
  
  Mixer.echo = function(text){
    if(Mixer.is_client_side()){
      
    }
  };
  
  Mixer.is_client_side = function(src){
    return Mixer.options == undefined || Mixer.options.mode == undefined || Mixer.options.mode == 'client');  
  };
  
  Mixer.client_include = function(src){
    s = Mixer.options.proxy == undefined ? src : Mixer.options.proxy + src;
    
    var req = new XMLHttpRequest();
    req.open('GET', s, false);
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
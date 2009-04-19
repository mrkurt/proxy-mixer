Mixer.append_raw_from_array(0);
// Including: mixer.js
Mixer.append_raw_from_array(4);
Mixer('header.html');
Mixer.append_raw_from_array(8);

      Mixer('nav.html', {
      	timeout: 200, //in ms
      	errors : {generic: 'Failed', not_found: 'Content not found', timeout: 'Content timed out'}
      });
    
Mixer.append_raw_from_array(12);
Mixer('footer.html');
Mixer.append_raw_from_array(16);

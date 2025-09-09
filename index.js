    const brinquedo = {
        'Rexbrinquedo': ['RATO', 'BOLA'],
        'Mimibrinquedo': ['BOLA', 'LASER'],
        'Fofobrinquedo': ['BOLA', 'RATO', 'LASER'],
        'Zerobrinquedo': ['RATO', 'BOLA'],
        'Bolabrinquedo': ['CAIXA', 'NOVELO'],
        'Bebebrinquedo': ['LASER', 'RATO', 'BOLA'],
        'Locobrinquedo': ['SKATE', 'RATO'],
    };

    const animais = {
      'Rex': { especie: 'cao', brinquedos: ['RATO', 'BOLA'] },
      'Mimi': { especie: 'gato', brinquedos: ['BOLA', 'LASER'] },
      'Fofo': { especie: 'gato', brinquedos: ['BOLA', 'RATO', 'LASER'] },
      'Zero': { especie: 'gato', brinquedos: ['RATO', 'BOLA'] },
      'Bola': { especie: 'cao', brinquedos: ['CAIXA', 'NOVELO'] },
      'Bebe': { especie: 'cao', brinquedos: ['LASER', 'RATO', 'BOLA'] },
      'Loco': { especie: 'jabuti', brinquedos: ['SKATE', 'RATO'] },
    };

    //for (const animal in animais) {
  //console.log(animais[animal]);

      if (( "Rex" in animais)&&('Rexbrinquedo' in brinquedo)) {
           console.log("cao melhor amigo do homem ");
       };
      if ( "Mimi" in animais) {
           console.log("gato o mais esperto dos animais");
       };
      if ( "Fofo" in animais) {
           console.log("gato o mais esperto dos animais");
       };
      if ( "Zero" in animais) {
           console.log("gato o mais esperto dos animais");
       };
      if ( "Bola" in animais) {
           console.log("cao melhor amigo do homem");
       };
      if ( "Bebe" in animais) {
           console.log("cao melhor amigo do homem");
       };
      if ( "Loco" in animais) {
           console.log("o mais paciente dos animais");
       };
       if ("cao" in animais) {
        console.log("REX");
       }



//}
    
    
    //brinquedosValidos = ['RATO', 'BOLA', 'LASER', 'NOVELO', 'CAIXA', 'SKATE'];

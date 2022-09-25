from util.scratch import pitch_to_freq

# Play sound
vm.system.sound.play(
    "/extra_files/Tadaa",
    freq=pitch_to_freq(
        vm.store.sound_pitch(),
        12000, # lowest frequency (lowest pitch)
        16000, # normal frequency (normal pitch)
        20000)) # highest frequency (highest pitch)

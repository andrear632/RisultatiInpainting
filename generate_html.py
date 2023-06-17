for i in [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
    tup = [str(i) for _ in range(40)]
    tup[10] = str(i) + "A"
    tup[11] = str(i) + "A"
    tup[12] = str(i) + "A"
    tup[25] = str(i) + "B"
    tup[26] = str(i) + "B"
    tup[27] = str(i) + "B"
    html = '''
        <div class="accordion-item">
            <h2 class="accordion-header">
                <button class="accordion-button collapsed fs-5" type="button" data-bs-toggle="collapse"
                    data-bs-target="#collapse%s" aria-expanded="false" aria-controls="collapse%s">
                    Audio clip %s: An emergency siren wailing as a large truck engine accelerates growing louder
                </button>
            </h2>
            <div id="collapse%s" class="accordion-collapse collapse collapsed">
                <div class="accordion-body">

                    <div class="container text-center">

                        <div class="row mt-2">
                            <div class="col-4 fs-4">
                                Original
                            </div>
                            <div class="col-4 fs-4">
                                Cut 1sec from 4.5s to 5.5s
                            </div>
                            <div class="col-4 fs-4">
                                Cut 2sec from 4s to 6s
                            </div>
                        </div>

                        <div class="row my-2">
                            <div class="col-4">
                                <img src="clip%s/original.png" class="w-75" alt="Original mel-spectrogram">
                            </div>
                            <div class="col-4">
                                <img src="clip%s/cut_1.png" class="w-75" alt="Cut 1s mel-spectrogram">
                            </div>
                            <div class="col-4">
                                <img src="clip%s/cut_2.png" class="w-75" alt="Cut 2s mel-spectrogram">
                            </div>
                        </div>

                        <div class="row mt-4">
                            <div class="col-4">
                                <audio controls>
                                    <source src="clip%s/original.wav" type="audio/wav">
                                    Your browser does not support the audio element.
                                </audio>
                            </div>
                            <div class="col-4">
                                <audio controls>
                                    <source src="clip%s/cut_1.wav">
                                    Your browser does not support the audio element.
                                </audio>
                            </div>
                            <div class="col-4">
                                <audio controls>
                                    <source src="clip%s/cut_2.wav" type="audio/wav">
                                    Your browser does not support the audio element.
                                </audio>
                            </div>
                        </div>

                        <div class="accordion mt-4">
                            <div class="accordion-item">
                                <h2 class="accordion-header">
                                    <button class="accordion-button collapsed fs-5" type="button"
                                        data-bs-toggle="collapse" data-bs-target="#collapse%s" aria-expanded="false"
                                        aria-controls="collapse%s">
                                        Mask 1 second from 4.5s to 5.5s
                                    </button>
                                </h2>
                                <div id="collapse%s" class="accordion-collapse collapse collapsed">
                                    <div class="accordion-body">


                                        <div class="row mt-4 text-center">
                                            <div class="col-2 fs-5">
                                                AudioLDM
                                            </div>
                                            <div class="col-2 fs-5">
                                                Tango (model) + AudioLDM (method)
                                            </div>
                                            <div class="col-2 fs-5">
                                                Tango + DDNM
                                            </div>
                                            <div class="col-2 fs-5">
                                                Tango + DDNM+
                                            </div>
                                            <div class="col-2 fs-5">
                                                Tango + RePaint
                                            </div>
                                            <div class="col-2 fs-5">
                                                Tango + RePaint Jump
                                            </div>
                                        </div>

                                        <div class="row my-2">
                                            <div class="col-2">
                                                <img src="clip%s/audioldm_1.png" class="w-100"
                                                    alt="AudioLDM mel-spectrogram">
                                            </div>
                                            <div class="col-2">
                                                <img src="clip%s/tango_1.png" class="w-100" alt="Tango mel-spectrogram">
                                            </div>
                                            <div class="col-2">
                                                <img src="clip%s/ddnm_1.png" class="w-100" alt="DDNM mel-spectrogram">
                                            </div>
                                            <div class="col-2">
                                                <img src="clip%s/ddnm+_1.png" class="w-100" alt="DDNM+ mel-spectrogram">
                                            </div>
                                            <div class="col-2">
                                                <img src="clip%s/repaint_1.png" class="w-100"
                                                    alt="RePaint mel-spectrogram">
                                            </div>
                                            <div class="col-2">
                                                <img src="clip%s/repaintjump_1.png" class="w-100"
                                                    alt="RePaint Jump mel-spectrogram">
                                            </div>
                                        </div>

                                        <div class="row mt-4">
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/audioldm_1.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/tango_1.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/ddnm_1.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/ddnm+_1.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/repaint_1.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/repaintjump_1.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>


                            <div class="accordion-item">
                                <h2 class="accordion-header">
                                    <button class="accordion-button collapsed fs-5" type="button"
                                        data-bs-toggle="collapse" data-bs-target="#collapse%s" aria-expanded="false"
                                        aria-controls="collapse%s">
                                        Mask 2 seconds from 4s to 6s
                                    </button>
                                </h2>
                                <div id="collapse%s" class="accordion-collapse collapse collapsed">
                                    <div class="accordion-body">

                                        <div class="row mt-4 text-center">
                                            <div class="col-2 fs-5">
                                                AudioLDM
                                            </div>
                                            <div class="col-2 fs-5">
                                                Tango (model) + AudioLDM (method)
                                            </div>
                                            <div class="col-2 fs-5">
                                                Tango + DDNM
                                            </div>
                                            <div class="col-2 fs-5">
                                                Tango + DDNM+
                                            </div>
                                            <div class="col-2 fs-5">
                                                Tango + RePaint
                                            </div>
                                            <div class="col-2 fs-5">
                                                Tango + RePaint Jump
                                            </div>
                                        </div>

                                        <div class="row my-2">
                                            <div class="col-2">
                                                <img src="clip%s/audioldm_2.png" class="w-100"
                                                    alt="AudioLDM mel-spectrogram">
                                            </div>
                                            <div class="col-2">
                                                <img src="clip%s/tango_2.png" class="w-100" alt="Tango mel-spectrogram">
                                            </div>
                                            <div class="col-2">
                                                <img src="clip%s/ddnm_2.png" class="w-100" alt="DDNM mel-spectrogram">
                                            </div>
                                            <div class="col-2">
                                                <img src="clip%s/ddnm+_2.png" class="w-100" alt="DDNM+ mel-spectrogram">
                                            </div>
                                            <div class="col-2">
                                                <img src="clip%s/repaint_2.png" class="w-100"
                                                    alt="RePaint mel-spectrogram">
                                            </div>
                                            <div class="col-2">
                                                <img src="clip%s/repaintjump_2.png" class="w-100"
                                                    alt="RePaint Jump mel-spectrogram">
                                            </div>
                                        </div>

                                        <div class="row mt-4">
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/audioldm_2.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/tango_2.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/ddnm_2.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/ddnm+_2.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/repaint_2.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                            <div class="col-2">
                                                <audio controls class="w-100">
                                                    <source src="clip%s/repaintjump_2.wav" type="audio/wav">
                                                    Your browser does not support the audio element.
                                                </audio>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        
                        



                    </div>
                </div>
            </div>
        </div>
    ''' % tuple(tup)
    f = open("out.txt", "a")
    f.write(html + "\n\n\n\n")
    f.close()
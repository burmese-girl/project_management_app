document.addEventListener('DOMContentLoaded', function() {
    const shuffleButton = document.querySelector('.shuffle-button');
    const playAllButton = document.querySelector('.play-all-button');
    const playPauseButton = document.querySelector('#play-pause-button');
    const trackList = document.querySelector('.track-list tbody');
    const audioTracks = Array.from(document.querySelectorAll('audio'));
    let currentTrackIndex = 0;
    let isPlaying = false;

    // Function to shuffle an array
    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }

    // Shuffle tracks function
    function shuffleTracks() {
        const shuffledTracks = shuffleArray(Array.from(trackList.querySelectorAll('tr')));
        trackList.innerHTML = '';
        shuffledTracks.forEach(function(track) {
            trackList.appendChild(track);
        });
    }

    // Function to play the current track
    function playTrack(index) {
        if (index >= 0 && index < audioTracks.length) {
            console.log("Playing track index:", index);
            audioTracks[index].play();
            audioTracks[index].addEventListener('ended', playNextTrack);
            isPlaying = true;
        }
    }

    // Play the next track in the list
    function playNextTrack() {
        currentTrackIndex++;
        if (currentTrackIndex < audioTracks.length) {
            playTrack(currentTrackIndex);
        } else {
            currentTrackIndex = 0;
            isPlaying = false;
            playPauseButton.textContent = 'Play';
        }
    }

    // Play all tracks in sequence
    function playAllTracks() {
        currentTrackIndex = 0;
        console.log("Play All =>", audioTracks.length);
        if (audioTracks.length > 0) {
            playTrack(currentTrackIndex);
        }
    }

    // Toggle play/pause button
    playPauseButton.addEventListener('click', function() {
        if (isPlaying) {
            audioTracks[currentTrackIndex].pause();
            isPlaying = false;
            playPauseButton.textContent = 'Play';
        } else {
            playTrack(currentTrackIndex);
            playPauseButton.textContent = 'Pause';
        }
    });

    // Add event listener to the shuffle button
    shuffleButton.addEventListener('click', shuffleTracks);

    // Add event listener to the play all button
    playAllButton.addEventListener('click', playAllTracks);
});

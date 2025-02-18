# EPTIC.V4

Workflow for future EPTIC updates.

## User part

1. database_tables contains a file "texts_for_test.xlsx" simulating the texts table in the database after an user has added IT to an existing event. Let's assume this is what we would find in SkEPTIC's database.

Text 1920 (written target) is the verbatim report; text 1855 (spoken target) has the metadata (including speaker and interpreter nativeness) but not the transcription; and we assume the spoken target video has been uploaded in /video and called "1855.mp4". **The video should be properly cut and in mp4 format** Texts like verb report and translation.

Therefore, the user did NOT add: transcription of oral part (in this case the interpretation), sentence splitting, alignments, interprer ID (this is done with diarization). Let's start with transcription.

2. Audio extraction. We need the audios for all spoken texts. Let's assume that, for every video in folder /video, if the video id is a spoken_written=SP AND texts.plain_text=NA, then it is new and we have to transcribe it. Therefore based on those conditions we extract the audios to 2. extracted_audios. As mentioned before we assume monolingual videos. We use the script `pipelines/extract_monolingual.py` and the audio file is outputed to `/2. extracted_audios`

3. Transcription is done automatically. Let's use WhisperX and output SRT to 3. output_subtitles. Can be done with GUI. Users review SRT files, then upload those. The user can now move on to another text.

## Developer part

4. before releasing a new version of the corpus, subtitles are converted into segmented sentences, plain text, automatically aligned. Diarization is performed. Code adjusted to check existing alignments to avoid overwriting.

5. export to pretgd with my code and tagged with NoSketch Engine



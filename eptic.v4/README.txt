# What about now?

This directory shows some features which make the code reusable in the future.

0. database_tables contains a file simulating the texts table in the database after an user has added texts to an existing event
(texts 2098 and 2162).

The user added: the metadata (Maybe automatic extaction could be added in future work), the verbatim report (Maybe automatic extaction could be added in future work), and the monolingual video.

The user did NOT add: transcription of oral part (in this case the interpretation), sentence splitting, alignments, diarization. maybe speaker gender and nativeness

1.
- Transcription is done automatically (in some way), along with timestamps. It is an XML file, so it can be edited easily (if sentences aren't ok etc).
script: I wrote a script for demonstration purposes. It could be a GUI...

2.
- At this point users review the ASR transcriptions (check errors and improve sentence splitting)...

3.
- the transcriptions are final and uploaded,

4. before releasing a new version of the corpus, texts are automatically aligned. Need code to check existing alignments to avoid overwriting.

5. exported to pretgd with my code and tagged with treetagger (add in future v4)


What is missing?

- texts.subtitled_text, the timestamps of the sentences
- sentence_split_text, an .xml with the sentence splitting
- texts.video_url, (not a feature in current DB, but hopefully will be added automatically)

Some new fields for the database (unrelated) like:

texts.source (default should be skeptic)
texts.has_video (0 or 1 depending if its there)
I think there might be others but this is out of the scope for now...

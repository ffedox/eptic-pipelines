# What about now?

This directory shows some features which make the code reusable in the future.

database_tables contains a file simulating the texts table in the database after an user has added a text to an existing event.

the workflow is the following:

1. database_tables contains sample files representing a possible future scenario:
- Metadata and verbatim report added by user
- Monolingual video added by user
- No transcription. 
- Transcription is done automatically (in some way), along with timestamps. It is an XML file, so it can be edited easily (if sentences aren't ok etc).
- At this point users review the ASR transcriptions (check errors and improve sentence splitting)...
- Once the transcriptions are final, they are automatically aligned. Need code to check existing alignments to avoid overwriting.
- ... (Maybe automatic extaction could be added in future work)
Texts are tagged with treetagger (add in future v4)


What is missing?

- texts.subtitled_text, the timestamps of the sentences
- sentence_split_text, an .xml with the sentence splitting
- texts.video_url, (not a feature in current DB, but hopefully will be added automatically)
- texts.interpreter_id, the diarization


Some new fields for the database (unrelated) like:

texts.source (default should be skeptic)
texts.has_video (0 or 1 depending if its there)
I think there might be others but this is out of the scope for now...

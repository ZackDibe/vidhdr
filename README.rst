The vidhdr module determines the mime type of video contained in a file or byte stream.

The vidhdr module defines the following function:

vidhdr.what(filepath[, buf])
  Tests the image data contained in the file located by *filepath*, and returns a string describing the image type. If optional *buf* is provided, the *filepath* is ignored and *buf* is assumed to contain the byte stream to test.

The following image types are recognized, as listed below with the return value from what():

=======================   ===================================================================
     Value                       Image format
=======================   ===================================================================
'video/x-m4v'                      Apple TV (.M4V)
'video/mp4'                      MPEG-4 (.MP4) Nero Mobile Profile
'various'                      MP4 w/ MPEG-7 Metadata [per ISO 14496-12]
'image/jpm'                      JPEG 2000 Compound Image (.JPM) [ISO 15444-6]
'video/3gpp2'                      3GPP2 EZmovie for KDDI 3G cellphones
'image/jpx'                      JPEG 2000 w/ extensions (.JPX) [ISO 15444-2]
'video/mp4'                      MP4 Base Media v2 [ISO 14496-12:2005]
'video/3gpp'                      3GPP Media (.3GP) Release 4
'video/x-m4v'                      Apple iPhone (.M4V)
'video/3gpp'                      3GPP Media (.3GP) Release 5
'video/mp4'                      MPEG-4 (.MP4) Nero Standard Profile
'video/mp4'                      MPEG-4 (.MP4) Nero Portable Profile
'video/mp4'                      H.264/MPEG-4 AVC (.MP4) Nero Standard Profile
'video/mp4'                      H.264/MPEG-4 AVC (.MP4) Nero Portable Profile
'image/jp2'                      JPEG 2000 Image (.JP2) [ISO 15444-1 ?]
'video/3gpp'                      3GPP Media (.3GP) Release 7 Streaming Servers
'audio/mp4'                      Apple iTunes AAC-LC (.M4P) AES Protected Audio
'video/mp4'                      MPEG-4 (.MP4) Nero HDTV Profile
'video/x-m4v'                      Apple iTunes Video (.M4V) Video
'various'                      MPEG-21 [ISO/IEC 21000-9]
'video/mp4'                      H.264/MPEG-4 AVC (.MP4) Nero Cinema Profile
'various'                      OMA DCF DRM Format 2.0 (OMA-TS-DRM-DCF-V2_0-20060303-A)
'audio/mp4'                      Apple iTunes AAC-LC (.M4B) Audio Book
'video/mp4'                      H.264/MPEG-4 AVC (.MP4) Nero HDTV Profile
'audio/x-m4a'                      Apple iTunes AAC-LC (.M4A) Audio
'video/mp4'                      H.264/MPEG-4 AVC (.MP4) Nero Mobile Profile
'video/vnd.dvb.file'             DVB (.DVB) over RTP
'various?'                      SD Memory Card Video
'video/mp4'                      MP4 v2 [ISO 14496-14]
'video/mp4'                      MP4 v1 [ISO 14496-1:ch13]
'video/mp4'                      Protected Video for Adobe Flash Player 9+ (.F4P)
'video/mp4'                      MPEG-4 (.MP4) Nero Cinema Profile
'video/mp4'                      MP4  Base Media v1 [IS0 14496-12:2003]
'various'                      Photo Player, MAF [ISO/IEC 23000-3]
'audio/mp4'                      MPEG-4 (.MP4) for SonyPSP
'video/mp4'                      MPEG-4/3GPP Mobile Profile (.MP4 / .3GP) (for NTT)
'video/vnd.dvb.file'             DVB (.DVB) over MPEG-2 Transport Stream
'video/quicktime'                Apple QuickTime (.MOV/QT)
'video/mp4'                      MP4 Base w/ AVC ext [ISO 14496-12:2005]
'video/mj2'                      Motion JPEG 2000 [ISO 15444-3] General Profile
'video/quicktime'                Sony / Mobile QuickTime (.MQV)  US Patent 7,477,830 (SonyCorp)
'video/3gpp'                      3GPP Release 6 General Profile
'video/mp4'                      Video for Adobe Flash Player 9+ (.F4V)
'video/3gpp'                      3GPP Media (.3GP) Release 2 (probably non-existent)
'video/3gpp'                      3GPP Media (.3GP) Release 3 (probably non-existent)
'video/3gpp'                      3GPP Media (.3GP) Release 1 (probably non-existent)
'video/3gpp'                      3GPP Media (.3GP) Release 6 Streaming Servers
'video/3gpp'                      3GPP (.3GP) Release 7 MBMS Extended Presentations
'video/3gpp'                      3GPP (.3GP) Release 6 MBMS Extended Presentations
'audio/mp4'                      Audio for Adobe Flash Player 9+ (.F4A)
'video/mj2'                      Motion JPEG 2000 [ISO 15444-3] Simple Profile
'audio/mp4'                      Audio Book for Adobe Flash Player 9+ (.F4B)
'audio/mp4'                      MP4 v2 [ISO 14496-14] Nero Digital AAC Audio
'video/3gpp2'                      3GPP2 Media (.3G2) compliant with 3GPP2 C.S0050-0 V1.0
'video/3gpp2'                      3GPP2 Media (.3G2) compliant with 3GPP2 C.S0050-A V1.0.0
'video/3gpp2'                      3GPP2 Media (.3G2) compliant with 3GPP2 C.S0050-B v1.0
=======================   ===================================================================


You can extend the list of file types vidhdr can recognize by appending to this variable:

vidhdr.tests
  A list of functions performing the individual tests. Each function takes two arguments: the byte-stream and an open file-like object. When what() is called with a byte-stream, the file-like object will be `None`.

  The test function should return a string describing the image type if the test succeeded, or `None` if it failed.

Example:

.. code-block:: python

  >>> import vidhdr
  >>> vidhdr.what('test.mp4')
  'video/mp4'

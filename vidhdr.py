"""Recognize video file mime type based on ftyp header. """

__all__ = ["what"]


VIDEO_TYPES = {
    'M4VH': {
        'mime-type': 'video/x-m4v',
        'description': 'Apple TV (.M4V)'
    },
    'NDSM': {
        'mime-type': 'video/mp4',
        'description': 'MPEG-4 (.MP4) Nero Mobile Profile'
    },
    'mp71': {
        'mime-type': 'various',
        'description': 'MP4 w/ MPEG-7 Metadata [per ISO 14496-12]'
    },
    'jpm': {
        'mime-type': 'image/jpm',
        'description': 'JPEG 2000 Compound Image (.JPM) [ISO 15444-6]'
    },
    'isc2': {
        'mime-type': '?/enc-isoff-generic',
        'description': 'ISMACryp 2.0 Encrypted File'
    },
    'KDDI': {
        'mime-type': 'video/3gpp2',
        'description': '3GPP2 EZmovie for KDDI 3G cellphones'
    },
    'jpx': {
        'mime-type': 'image/jpx',
        'description': 'JPEG 2000 w/ extensions (.JPX) [ISO 15444-2]'
    },
    'iso2': {
        'mime-type': 'video/mp4',
        'description': 'MP4 Base Media v2 [ISO 14496-12:2005]'
    },
    '3gp4': {
        'mime-type': 'video/3gpp',
        'description': '3GPP Media (.3GP) Release 4'
    },
    'M4VP': {
        'mime-type': 'video/x-m4v',
        'description': 'Apple iPhone (.M4V)'
    },
    '3gp5': {
        'mime-type': 'video/3gpp',
        'description': '3GPP Media (.3GP) Release 5'
    },
    'NDSS': {
        'mime-type': 'video/mp4',
        'description': 'MPEG-4 (.MP4) Nero Standard Profile'
    },
    'NDSP': {
        'mime-type': 'video/mp4',
        'description': 'MPEG-4 (.MP4) Nero Portable Profile'
    },
    'NDXS': {
        'mime-type': 'video/mp4',
        'description': 'H.264/MPEG-4 AVC (.MP4) Nero Standard Profile'
    },
    'NDXP': {
        'mime-type': 'video/mp4',
        'description': 'H.264/MPEG-4 AVC (.MP4) Nero Portable Profile'
    },
    'JP2': {
        'mime-type': 'image/jp2',
        'description': 'JPEG 2000 Image (.JP2) [ISO 15444-1 ?]'
    },
    '3gs7': {
        'mime-type': 'video/3gpp',
        'description': '3GPP Media (.3GP) Release 7 Streaming Servers'
    },
    'M4P': {
        'mime-type': 'audio/mp4',
        'description': 'Apple iTunes AAC-LC (.M4P) AES Protected Audio'
    },
    'NDSH': {
        'mime-type': 'video/mp4',
        'description': 'MPEG-4 (.MP4) Nero HDTV Profile'
    },
    'M4V': {
        'mime-type': 'video/x-m4v',
        'description': 'Apple iTunes Video (.M4V) Video'
    },
    'mp21': {
        'mime-type': 'various',
        'description': 'MPEG-21 [ISO/IEC 21000-9]'
    },
    'NDXC': {
        'mime-type': 'video/mp4',
        'description': 'H.264/MPEG-4 AVC (.MP4) Nero Cinema Profile'
    },
    'odcf': {
        'mime-type': 'various',
        'description': 'OMA DCF DRM Format 2.0 (OMA-TS-DRM-DCF-V2_0-20060303-A)'
    },
    'M4B': {
        'mime-type': 'audio/mp4',
        'description': 'Apple iTunes AAC-LC (.M4B) Audio Book'
    },
    'NDXH': {
        'mime-type': 'video/mp4',
        'description': 'H.264/MPEG-4 AVC (.MP4) Nero HDTV Profile'
    },
    'M4A': {
        'mime-type': 'audio/x-m4a',
        'description': 'Apple iTunes AAC-LC (.M4A) Audio'
    },
    'NDXM': {
        'mime-type': 'video/mp4',
        'description': 'H.264/MPEG-4 AVC (.MP4) Nero Mobile Profile'
    },
    'dvr1': {
        'mime-type': 'video/vnd.dvb.file',
        'description': 'DVB (.DVB) over RTP'
    },
    'sdv': {
        'mime-type': 'various?',
        'description': 'SD Memory Card Video'
    },
    'mp42': {
        'mime-type': 'video/mp4',
        'description': 'MP4 v2 [ISO 14496-14]'
    },
    'mp41': {
        'mime-type': 'video/mp4',
        'description': 'MP4 v1 [ISO 14496-1:ch13]'
    },
    'F4P': {
        'mime-type': 'video/mp4',
        'description': 'Protected Video for Adobe Flash Player 9+ (.F4P)'
    },
    'NDSC': {
        'mime-type': 'video/mp4',
        'description': 'MPEG-4 (.MP4) Nero Cinema Profile'
    },
    'isom': {
        'mime-type': 'video/mp4',
        'description': 'MP4  Base Media v1 [IS0 14496-12:2003]'
    },
    'MPPI': {
        'mime-type': 'various',
        'description': 'Photo Player, MAF [ISO/IEC 23000-3]'
    },
    'MSNV': {
        'mime-type': 'audio/mp4',
        'description': 'MPEG-4 (.MP4) for SonyPSP'
    },
    'mmp4': {
        'mime-type': 'video/mp4',
        'description': 'MPEG-4/3GPP Mobile Profile (.MP4 / .3GP) (for NTT)'
    },
    'dvt1': {
        'mime-type': 'video/vnd.dvb.file',
        'description': 'DVB (.DVB) over MPEG-2 Transport Stream'
    },
    'qt': {
        'mime-type': 'video/quicktime',
        'description': 'Apple QuickTime (.MOV/QT)'
    },
    'avc1': {
        'mime-type': 'video/mp4',
        'description': 'MP4 Base w/ AVC ext [ISO 14496-12:2005]'
    },
    'mjp2': {
        'mime-type': 'video/mj2',
        'description': 'Motion JPEG 2000 [ISO 15444-3] General Profile'
    },
    'mqt': {
        'mime-type': 'video/quicktime',
        'description': 'Sony / Mobile QuickTime (.MQV)  US Patent 7,477,830 (Sony Corp)'
    },
    '3gg6': {
        'mime-type': 'video/3gpp',
        'description': '3GPP Release 6 General Profile'
    },
    'F4V': {
        'mime-type': 'video/mp4',
        'description': 'Video for Adobe Flash Player 9+ (.F4V)'
    },
    '3gp2': {
        'mime-type': 'video/3gpp',
        'description': '3GPP Media (.3GP) Release 2 (probably non-existent)'
    },
    '3gp3': {
        'mime-type': 'video/3gpp',
        'description': '3GPP Media (.3GP) Release 3 (probably non-existent)'
    },
    '3gp1': {
        'mime-type': 'video/3gpp',
        'description': '3GPP Media (.3GP) Release 1 (probably non-existent)'
    },
    '3gp6': {
        'mime-type': 'video/3gpp',
        'description': '3GPP Media (.3GP) Release 6 Streaming Servers'
    },
    '3ge7': {
        'mime-type': 'video/3gpp',
        'description': '3GPP (.3GP) Release 7 MBMS Extended Presentations'
    },
    '3ge6': {
        'mime-type': 'video/3gpp',
        'description': '3GPP (.3GP) Release 6 MBMS Extended Presentations'
    },
    'F4A': {
        'mime-type': 'audio/mp4',
        'description': 'Audio for Adobe Flash Player 9+ (.F4A)'
    },
    'mj2s': {
        'mime-type': 'video/mj2',
        'description': 'Motion JPEG 2000 [ISO 15444-3] Simple Profile'
    },
    'F4B': {
        'mime-type': 'audio/mp4',
        'description': 'Audio Book for Adobe Flash Player 9+ (.F4B)'
    },
    'NDAS': {
        'mime-type': 'audio/mp4',
        'description': 'MP4 v2 [ISO 14496-14] Nero Digital AAC Audio'
    },
    'dmpf': {
        'mime-type': 'various',
        'description': 'Digital Media Project'
    },
    '3g2a': {
        'mime-type': 'video/3gpp2',
        'description': '3GPP2 Media (.3G2) compliant with 3GPP2 C.S0050-0 V1.0'
    },
    '3g2b': {
        'mime-type': 'video/3gpp2',
        'description': '3GPP2 Media (.3G2) compliant with 3GPP2 C.S0050-A V1.0.0'
    },
    '3g2c': {
        'mime-type': 'video/3gpp2',
        'description': '3GPP2 Media (.3G2) compliant with 3GPP2 C.S0050-B v1.0'
    }
}


tests = []


def what(fpath, buf=None):
    """
    Args:
        fpath (str): path of the file to open and check
        buf (str): byte stream of the file to check
                   fpath is ignored if buf is provided
    Returns:
        str. mime type of the file or None if unknown/not a video
    """

    fd = None
    try:
        if buf is None:
            if isinstance(fpath, basestring):
                fd = open(fpath, 'rb')
                buf = fd.read(32)
            else:
                location = fpath.tell()
                buf = fpath.read(32)
                fpath.seek(location)
        for tf in tests:
            res = tf(buf, fd)
            if res:
                return res
    finally:
        if fd:
            fd.close()

    return None


def test_ftyp(buf, fd):
    ftyp = buf[8:12].strip()
    video_type = VIDEO_TYPES.get(ftyp, {})
    return video_type.get('mime-type')

tests.append(test_ftyp)

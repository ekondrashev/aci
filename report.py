#!/usr/bin/env python3
'''
Doc
'''
import argparse
import json
import logging
from os.path import basename

import mail

__author__ = 'Eugene Kondrashev'
__email__ = 'eugene.kondrashev@gmail.com'

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--build-log", default='log.txt')
parser.add_argument("-p", "--payload", default='payload.json')
parser.add_argument("-r", "--retcode", type=int)

parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true", default=True)


def main(args):

    with open(args.payload, "rb") as f:
        payload_content = f.read()
    payload = json.loads(payload_content)
    repo = payload.get('repository', {}).get('name')
    pusher = payload.get('pusher', {}).get('email')
    subj = 'Build %s for %s by %s' % ('succeeded' if args.retcode == 0 else 'failed', repo, pusher)

    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.utils import formatdate
    recipients = ('eugene.kondrashev@gmail.com', )
    msg = MIMEMultipart(
        From=mail.USER,
        To=", ".join(recipients),
        Date=formatdate(localtime=True),
    )
    msg['Subject'] = subj
    msg.attach(MIMEText(payload_content))
    with open(args.build_log, "rb") as fil:
        content = fil.read()
        msg.attach(MIMEApplication(
            content,
            Content_Disposition='attachment; filename="%s"' % basename(args.build_log),
            Name=basename(args.build_log)
        ))
    mail.sendmsg(recipients, msg)

if __name__ == '__main__':
    args = parser.parse_args()
    if args.verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(
#         filename=args.log,
        format="%(asctime)s %(levelname)s:%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=level
    )
    main(args)


from django.core.management.base import BaseCommand, CommandError

from silverstrike.lib import import_ofx


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file',
            type=str,
            help='OFX/QFX file to import')

    def handle(self, *args, **options):
        try:
            result = import_ofx(options['file'])
        except FileNotFoundError:
            raise CommandError('Could not open {} file'.format(options['file']))
        else:
            print('Imported: {}'.format(len(result['imported'])))
            print('Skipped: {}'.format(len(result['skipped'])))
            print('Failed: {}'.format(len(result['failed'])))

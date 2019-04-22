#!/usr/bin/env python
# coding=utf-8

# Author:cage
# forms.py 2019-04-14 23:56

class FormMixin(object):
    def get_errors(self):
        if hasattr(self, 'errors'):
            errors = self.errors.get_json_data()
            new_errors = {}
            for key, message_dicts in errors.items():
                print(errors)
                messages = []
                for message in message_dicts:
                    print(message)
                    print(message_dicts)
                    messages.append(message['message'])
                new_errors[key] = messages
            return new_errors
        else:
            return {}





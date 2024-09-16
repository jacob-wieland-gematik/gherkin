def source_event(path):
    event = {
        'source': {
            'uri': path,
            'data': open(path, encoding='utf8', newline='').read(),
            'mediaType': 'text/x.cucumber.gherkin+plain'
        }
    }
    return event

class SourceEvents:
    def __init__(self, paths):
        self.paths = paths

    def enum(self):
        return map(source_event, self.paths)

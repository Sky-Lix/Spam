import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
MicroTardis filters
===================

A couple of useful microscopy file formats: .spc (EDAX) and .tif (from Nova NanoSEM, Quanta200, Philips XL30)

```
cd /opt/mytardis/current/tardis/apps

git clone https://github.com/stevage/MicroTardis-filters

mv MicroTardis-filters microtardis

# The filters have dependencies like PIL.
# Hopefully we'll find a better way of handling this.

cp microtardis/buildout-microtardis.cfg /opt/mytardis/current/

cat >> ../settings.py <<EOF

try:
    POST_SAVE_FILTERS
except:
    POST_SAVE_FILTERS = []

POST_SAVE_FILTERS += [
    ("tardis.apps.microtardis.filters.exiftags.make_filter", ["MICROSCOPY_EXIF","http://rmmf.isis.rmit.edu.au/schemas"]),
    ("tardis.apps.microtardis.filters.spctags.make_filter", ["EDAXGenesis_SPC","http://rmmf.isis.rmit.edu.au/schemas"]),
    ]

EOF


# Do NOT add the "app" to INSTALLED_APPS. You'll ruin everything. (Currently the 'app' part is broken. Very broken.)

cd /opt/mytardis/current

bin/buildout -c buildout-microtardis.cfg

# All done
```
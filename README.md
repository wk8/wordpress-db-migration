WordPress DB migration
======================

It can be a pain to migrate your WordPress website from your dev environment to
another one, or to change your domain name.

This little script's goal is to make it easy: just export the DB to a SQL file,
then run

```
./wp-db-migrate.py --from '<OLD_URL>' --to '<NEW_URL>' --in '<path/to/old_db.sql>' --out '<path/to/new_db.sql>'
```

For example to deploy your dev copy on `localhost/my_site` to your live site at
`my_site.com`, assuming you have a dumb of your dev DB at `~/my_site/dump.sql`:
```
./wp-db-migrate.py --from 'http://localhost/my_site' --to 'http://my_site.com' --in '~/my_site/dump.sql' --out '/tmp/migrated_dump.sql'
```
will create `/tmp/migrated_dump.sql` with the migrated DB you then just need to import into your live server(s).

Note that the input file (old DB file) won't be modified in any way, but the
output file (new DB) will be overwritten if it exists.

It's a very simple script, but I always welcome feedback, pull requests, bug
reports...

***A few details***

Migrates both string data and 'serialized' (in the WordPress sense) data.

Processes the input file in linear time and constant memory.

Note that I'm aware that WordPress offers a functionality to do just that, but
you do need to have access to the running site to do it, which is not always
the case (old dev copy, or else long-lost domain name...)
And even if you do have access to a running instance, this allows to script it!

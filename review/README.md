# Re:VIEW でのタイムラインを描画するためのサンプル

https://reviewml.org/ja/

## Re:VIEW のセットアップ

```bash
# apt-get install texlive-lang-japanese texlive-pictures
```

```bash
$ bundle install
Fetching gem metadata from https://rubygems.org/....
Resolving dependencies...
Fetching rouge 4.3.0
Fetching rubyzip 2.3.2
Fetching image_size 3.4.0
Fetching tty-color 0.6.0
Fetching strscan 3.1.0
Installing tty-color 0.6.0
Installing strscan 3.1.0 with native extensions
Installing rubyzip 2.3.2
Fetching pastel 0.8.0
Installing image_size 3.4.0
Installing rouge 4.3.0
Installing pastel 0.8.0
Fetching tty-logger 0.6.0
Installing tty-logger 0.6.0
Fetching rexml 3.3.2
Installing rexml 3.3.2
Fetching review 5.9.0
Installing review 5.9.0
Bundle complete! 1 Gemfile dependency, 10 gems now installed.
Bundled gems are installed into `./vendor/bundle`
Post-install message from rubyzip:
RubyZip 3.0 is coming!
**********************

The public API of some Rubyzip classes has been modernized to use named
parameters for optional arguments. Please check your usage of the
following classes:
  * `Zip::File`
  * `Zip::Entry`
  * `Zip::InputStream`
  * `Zip::OutputStream`

Please ensure that your Gemfiles and .gemspecs are suitably restrictive
to avoid an unexpected breakage when 3.0 is released (e.g. ~> 2.3.0).
See https://github.com/rubyzip/rubyzip for details. The Changelog also
lists other enhancements and bugfixes that have been implemented since
version 2.3.0.
$
```

```bash
$ kanji-config-updmap status
CURRENT family for ja: noEmbed (variant: <empty>)
Standby family : haranoaji
Standby family : ipa
Standby family : ipaex
$ sudo kanji-config-updmap-sys --jis2004 haranoaji
Setting up ... haranoaji for ja
Creating new config file /etc/texmf/web2c/updmap.cfg
updmap will read the following updmap.cfg files (in precedence order):
  /etc/texmf/web2c/updmap.cfg
  /usr/share/texmf/web2c/updmap.cfg
  /usr/share/texlive/texmf-dist/web2c/updmap.cfg
updmap may write changes to the following updmap.cfg file:
  /etc/texmf/web2c/updmap.cfg
dvips output dir: "/var/lib/texmf/fonts/map/dvips/updmap"
pdftex output dir: "/var/lib/texmf/fonts/map/pdftex/updmap"
dvipdfmx output dir: "/var/lib/texmf/fonts/map/dvipdfmx/updmap"

updmap is creating new map files
using the following configuration:
  LW35 font names                  : URWkb (default)
  prefer outlines                  : true (default)
  texhash enabled                  : true
  download standard fonts (dvips)  : true (default)
  download standard fonts (pdftex) : true (default)
  jaEmbed replacement string       : haranoaji (/etc/texmf/web2c/updmap.cfg)
  jaVariant replacement string     : -04 (/etc/texmf/web2c/updmap.cfg)
  scEmbed replacement string       : noEmbed (default)
  tcEmbed replacement string       : noEmbed (default)
  koEmbed replacement string       : noEmbed (default)
  create a mapfile for pxdvi       : false (default)

Scanning for LW35 support files  [  3 files]
Scanning for MixedMap entries    [ 18 files]
Scanning for KanjiMap entries    [ 11 files]
Scanning for Map entries         [ 60 files]

Generating output for dvipdfmx...
Generating output for ps2pk...
Generating output for dvips...
Generating output for pdftex...

Files generated:
  /var/lib/texmf/fonts/map/dvips/updmap:
       15758 2024-08-01 15:10:11 builtin35.map
       21231 2024-08-01 15:10:11 download35.map
      226676 2024-08-01 15:10:11 psfonts_pk.map
      239697 2024-08-01 15:10:11 psfonts_t1.map
      230477 2024-08-01 15:10:11 ps2pk.map
      239697 2024-08-01 15:10:11 psfonts.map = psfonts_t1.map
  /var/lib/texmf/fonts/map/pdftex/updmap:
      230484 2024-08-01 15:10:11 pdftex_dl14.map
      228819 2024-08-01 15:10:11 pdftex_ndl14.map
      230484 2024-08-01 15:10:11 pdftex.map = pdftex_dl14.map
  /var/lib/texmf/fonts/map/dvipdfmx/updmap:
       10040 2024-08-01 15:10:11 kanjix.map

Transcript written on: /var/lib/texmf/web2c/updmap.log
updmap: updating ls-R files.
$ kanji-config-updmap status
CURRENT family for ja: haranoaji (variant: -04)
Standby family : haranoaji
Standby family : ipa
Standby family : ipaex
$
```

## Re:VIEW の設定

```diff
$ diff -u config.yml.orig config.yml
--- config.yml.orig     2024-08-01 11:16:06.300525087 +0900
+++ config.yml  2024-08-04 13:43:33.511738334 +0900
@@ -357,7 +357,7 @@
   # epubmaker:階層を使うものはここまで

 # LaTeX用のスタイルファイル(styディレクトリ以下に置くこと)
-texstyle: ["reviewmacro"]
+texstyle: ["reviewmacro", "timeline"]
 #
 # LaTeX用のdocumentclassを指定する
 # オプションについてはsty/README.mdを参照
$
```

## PDF の生成

```bash
$ cd example
$ bundle exec --gemfile=../Gemfile rake pdf
review-pdfmaker  config.yml
ℹ INFO    compiling example.tex
ℹ INFO    uplatex -interaction=nonstopmode -file-line-error -halt-on-error __REVIEW_BOOK__.tex
ℹ INFO    uplatex -interaction=nonstopmode -file-line-error -halt-on-error __REVIEW_BOOK__.tex
ℹ INFO    uplatex -interaction=nonstopmode -file-line-error -halt-on-error __REVIEW_BOOK__.tex
ℹ INFO    dvipdfmx -d 5 -z 9 __REVIEW_BOOK__.dvi
✔ SUCCESS built book.pdf
```

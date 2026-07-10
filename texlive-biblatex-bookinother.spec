%global tl_name biblatex-bookinother
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3.3
Release:	%{tl_revision}.1
Summary:	Manage book edited in other entry type
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-bookinother
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bookinother.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bookinother.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides new BibLaTeX entry types and fields for book
edited in other types, like for instance @bookinarticle. It offers more
types than the older package biblatex-bookinarticle which it supersedes.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-bookinother
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/biblatex-bookinother.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/biblatex-bookinother.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinarticle.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinarticle.dot
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinarticle.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookincollection.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookincollection.dot
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookincollection.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookininarticle.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookininarticle.dot
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookininarticle.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookininbook.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookininbook.dot
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookininbook.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinincollection.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinincollection.dot
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinincollection.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookininproceedings.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookininproceedings.dot
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookininproceedings.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinjournal.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinjournal.dot
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinjournal.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinproceedings.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinproceedings.dot
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinproceedings.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinthesis.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinthesis.dot
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/example-bookinthesis.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/generate-crossref-graphs.py
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/latexmkrc
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/documentation/makefile
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinother/makefile
%{_datadir}/texmf-dist/tex/latex/biblatex-bookinother/bookinother.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-bookinother/bookinother.dbx

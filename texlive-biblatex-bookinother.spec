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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides new BibLaTeX entry types and fields for book
edited in other types, like for instance @bookinarticle. It offers more
types than the older package biblatex-bookinarticle which it supersedes.


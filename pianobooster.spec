Name:           pianobooster
Version:        0.7.2b
Release:        1%{?dist}
Summary:        A MIDI file player that teaches you how to play the piano

License:        GPLv3+
URL:            https://github.com/captnfab/PianoBooster
Source0:        https://github.com/captnfab/PianoBooster/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(rtmidi)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  hicolor-icon-theme

Requires:       dejavu-sans-fonts
Requires:       unzip
Requires:       hicolor-icon-theme
Requires:       libnotify

Recommends:     qt5-qttranslations

%description
A MIDI file player/game that displays the musical notes AND teaches you how
to play the piano. 
 
PianoBooster is a fun way of playing along with a musical accompaniment and
at the same time learning the basics of reading musical notation.
The difference between playing along to a CD or a standard MIDI file
is that PianoBooster listens and reacts to what you are playing on a
MIDI keyboard.

%prep
%autosetup -n PianoBooster-%{version}

%build
%cmake \
 -DUSE_SYSTEM_FONT=ON \
 -DNO_DOCS=ON \
 -DNO_LICENSE=ON \
 -DNO_CHANGELOG=ON \
 -DWITH_MAN=ON

%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%license license.txt gplv3.txt
%doc README.md Changelog.txt doc/faq.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/music
%dir %{_datadir}/games/%{name}/translations
%{_datadir}/games/%{name}/music/*.zip
%{_datadir}/games/%{name}/translations/%{name}*.qm
%{_datadir}/games/%{name}/translations/music*.qm
%{_datadir}/games/%{name}/translations/*.json
%{_mandir}/man6/%{name}.6*

%changelog
* Fri Mar 20 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.7.2b-1
- Initial build

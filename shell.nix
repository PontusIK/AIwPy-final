{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    (pkgs.python312.withPackages(p: with p; [
      scipy
      keras
      tkinter
      pillow
      opencv4
    ]))
  ];
}

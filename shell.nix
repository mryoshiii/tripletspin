{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

  packages = [
  (pkgs.python313.withPackages(pypkgs: with pypkgs; [
    requests
    pip
    pytelegrambotapi
    # countryflag
    ]))
   ];

}

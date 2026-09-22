# Voxel Red Preview

A sealed **Pokémon FireRed** cart using **Battle Art 1.21.0**, for
**Gen1Recomp 0.2.73 or newer**. Download the `.g1rcart` from
[Releases](https://github.com/notquiteog/VoxelRed/releases), install it from
the launcher and supply your own supported FireRed game data. No ROM included.

This first preview includes **only Battle Art**. Overworld Spawns, Online+,
Dramatic Sky Ride and Double Battles are not included: their FireRed ports
and integration checks are unfinished. They remain independent projects.

Includes native-art plants, reviewed building exteriors, modeled terrain,
render distance choices and contextual boundaries, home/lab/Mart/Center
interior dioramas, free cameras and native battles over 3D scenery.

103 specialty FireRed interior maps retain native presentation. Battle
Pokémon remain native screen sprites; full depth-positioned battles and
complete Gamma Emerald parity are unfinished. Native healing/shop/special
animation fallbacks remain active. This preview does not change FireRed’s
native battle simulation or add wild doubles or multiplayer.

The exact version and SHA-256 are pinned in `cart.json`. The cartridge contains
only its manifest, and downloads the published mod when installed.

To rebuild with an engine checkout, run:

```sh
python3 tools/cartkit_firered.py /path/to/gen1recomp/tools/cartkit.py pack . -o voxel_red-0.1.0.g1rcart
```

The wrapper adds FireRed to older cartkit versions' base list; it changes no
runtime rules. The packed cartridge was accepted and booted by engine 0.2.73.
Release QA checked the exact single mod pin, a Center interior, static/first/
rotating cameras and return to Pallet. This is representative preview QA,
not an exhaustive FireRed playthrough.

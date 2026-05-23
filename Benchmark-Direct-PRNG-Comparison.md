# Direct PRNG comparison

The following 30 pseudorandom numbers generators (PRNG) have been tested to generate pseudorandom numbers (PRN) according to **exponential**, **log-normal**, **gamma** and **triangular** distribution:

* ThreadLocalRandom
* Random
* SecureRandom
* Well512a
* Well1024a
* Well19937a
* Well19937c
* Well44497a
* Well44497b
* MersenneTwister
* ISAAC
* XoRoShiRo128++
* XoRoShiRo128**
* XoRoShiRo64**
* XoRoShiRo256++
* XoRoShiRo1024++
* XoRoShiRo1024*
* XoRoShiRo1024**
* L32X64Mix
* L64X128Mix
* L64X128
* L64X256Mix
* L64X1024Mix
* L128X128Mix
* L128X256Mix
* L128X1024Mix
* PcgRxsMXs64
* Philox4x64
* Drand48
* Drand48Mix

## Error between theoretical values and values after 10<sup>8</sup>. generated PRN

### Mean value of the generated PRN

<table id="T_052c9">
  <caption>Mean Error (in %)</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_052c9_level0_col0" class="col_heading level0 col0" >Exponential</th>
      <th id="T_052c9_level0_col1" class="col_heading level0 col1" >Logarithmic</th>
      <th id="T_052c9_level0_col2" class="col_heading level0 col2" >Gamma</th>
      <th id="T_052c9_level0_col3" class="col_heading level0 col3" >Triangular</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_052c9_level0_row0" class="row_heading level0 row0" >ThreadLocalRandom</th>
      <td id="T_052c9_row0_col0" class="data row0 col0" >0.00009%</td>
      <td id="T_052c9_row0_col1" class="data row0 col1" >0.00049%</td>
      <td id="T_052c9_row0_col2" class="data row0 col2" >0.00013%</td>
      <td id="T_052c9_row0_col3" class="data row0 col3" >0.00003%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row1" class="row_heading level0 row1" >Random</th>
      <td id="T_052c9_row1_col0" class="data row1 col0" >0.00170%</td>
      <td id="T_052c9_row1_col1" class="data row1 col1" >0.00012%</td>
      <td id="T_052c9_row1_col2" class="data row1 col2" >0.00100%</td>
      <td id="T_052c9_row1_col3" class="data row1 col3" >0.00015%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row2" class="row_heading level0 row2" >SecureRandom</th>
      <td id="T_052c9_row2_col0" class="data row2 col0" >0.00055%</td>
      <td id="T_052c9_row2_col1" class="data row2 col1" >0.00065%</td>
      <td id="T_052c9_row2_col2" class="data row2 col2" >0.00010%</td>
      <td id="T_052c9_row2_col3" class="data row2 col3" >0.00014%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row3" class="row_heading level0 row3" >Well512a</th>
      <td id="T_052c9_row3_col0" class="data row3 col0" >0.00099%</td>
      <td id="T_052c9_row3_col1" class="data row3 col1" >0.00021%</td>
      <td id="T_052c9_row3_col2" class="data row3 col2" >0.00021%</td>
      <td id="T_052c9_row3_col3" class="data row3 col3" >0.00028%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row4" class="row_heading level0 row4" >Well1024a</th>
      <td id="T_052c9_row4_col0" class="data row4 col0" >0.00100%</td>
      <td id="T_052c9_row4_col1" class="data row4 col1" >0.00010%</td>
      <td id="T_052c9_row4_col2" class="data row4 col2" >0.00038%</td>
      <td id="T_052c9_row4_col3" class="data row4 col3" >0.00017%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row5" class="row_heading level0 row5" >Well19937a</th>
      <td id="T_052c9_row5_col0" class="data row5 col0" >0.00056%</td>
      <td id="T_052c9_row5_col1" class="data row5 col1" >0.00063%</td>
      <td id="T_052c9_row5_col2" class="data row5 col2" >0.00009%</td>
      <td id="T_052c9_row5_col3" class="data row5 col3" >0.00050%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row6" class="row_heading level0 row6" >Well19937c</th>
      <td id="T_052c9_row6_col0" class="data row6 col0" >0.00101%</td>
      <td id="T_052c9_row6_col1" class="data row6 col1" >0.00022%</td>
      <td id="T_052c9_row6_col2" class="data row6 col2" >0.00009%</td>
      <td id="T_052c9_row6_col3" class="data row6 col3" >0.00041%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row7" class="row_heading level0 row7" >Well44497a</th>
      <td id="T_052c9_row7_col0" class="data row7 col0" >0.00056%</td>
      <td id="T_052c9_row7_col1" class="data row7 col1" >0.00018%</td>
      <td id="T_052c9_row7_col2" class="data row7 col2" >0.00080%</td>
      <td id="T_052c9_row7_col3" class="data row7 col3" >0.00008%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row8" class="row_heading level0 row8" >Well44497b</th>
      <td id="T_052c9_row8_col0" class="data row8 col0" >0.00049%</td>
      <td id="T_052c9_row8_col1" class="data row8 col1" >0.00029%</td>
      <td id="T_052c9_row8_col2" class="data row8 col2" >0.00019%</td>
      <td id="T_052c9_row8_col3" class="data row8 col3" >0.00088%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row9" class="row_heading level0 row9" >MersenneTwister</th>
      <td id="T_052c9_row9_col0" class="data row9 col0" >0.00014%</td>
      <td id="T_052c9_row9_col1" class="data row9 col1" >0.00031%</td>
      <td id="T_052c9_row9_col2" class="data row9 col2" >0.00066%</td>
      <td id="T_052c9_row9_col3" class="data row9 col3" >0.00023%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row10" class="row_heading level0 row10" >SFC64</th>
      <td id="T_052c9_row10_col0" class="data row10 col0" >0.00159%</td>
      <td id="T_052c9_row10_col1" class="data row10 col1" >0.00024%</td>
      <td id="T_052c9_row10_col2" class="data row10 col2" >0.00041%</td>
      <td id="T_052c9_row10_col3" class="data row10 col3" >0.00042%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row11" class="row_heading level0 row11" >ISAAC</th>
      <td id="T_052c9_row11_col0" class="data row11 col0" >0.00008%</td>
      <td id="T_052c9_row11_col1" class="data row11 col1" >0.00021%</td>
      <td id="T_052c9_row11_col2" class="data row11 col2" >0.00024%</td>
      <td id="T_052c9_row11_col3" class="data row11 col3" >0.00027%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row12" class="row_heading level0 row12" >XoRoShiRo128++</th>
      <td id="T_052c9_row12_col0" class="data row12 col0" >0.00062%</td>
      <td id="T_052c9_row12_col1" class="data row12 col1" >0.00005%</td>
      <td id="T_052c9_row12_col2" class="data row12 col2" >0.00048%</td>
      <td id="T_052c9_row12_col3" class="data row12 col3" >0.00001%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row13" class="row_heading level0 row13" >XoRoShiRo128**</th>
      <td id="T_052c9_row13_col0" class="data row13 col0" >0.00109%</td>
      <td id="T_052c9_row13_col1" class="data row13 col1" >0.00025%</td>
      <td id="T_052c9_row13_col2" class="data row13 col2" >0.00078%</td>
      <td id="T_052c9_row13_col3" class="data row13 col3" >0.00018%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row14" class="row_heading level0 row14" >XoRoShiRo64**</th>
      <td id="T_052c9_row14_col0" class="data row14 col0" >0.00022%</td>
      <td id="T_052c9_row14_col1" class="data row14 col1" >0.00002%</td>
      <td id="T_052c9_row14_col2" class="data row14 col2" >0.00003%</td>
      <td id="T_052c9_row14_col3" class="data row14 col3" >0.00038%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row15" class="row_heading level0 row15" >XoRoShiRo256++</th>
      <td id="T_052c9_row15_col0" class="data row15 col0" >0.00063%</td>
      <td id="T_052c9_row15_col1" class="data row15 col1" >0.00003%</td>
      <td id="T_052c9_row15_col2" class="data row15 col2" >0.00025%</td>
      <td id="T_052c9_row15_col3" class="data row15 col3" >0.00052%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row16" class="row_heading level0 row16" >XoRoShiRo1024++</th>
      <td id="T_052c9_row16_col0" class="data row16 col0" >0.00006%</td>
      <td id="T_052c9_row16_col1" class="data row16 col1" >0.00041%</td>
      <td id="T_052c9_row16_col2" class="data row16 col2" >0.00050%</td>
      <td id="T_052c9_row16_col3" class="data row16 col3" >0.00032%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row17" class="row_heading level0 row17" >XoRoShiRo1024*</th>
      <td id="T_052c9_row17_col0" class="data row17 col0" >0.00061%</td>
      <td id="T_052c9_row17_col1" class="data row17 col1" >0.00034%</td>
      <td id="T_052c9_row17_col2" class="data row17 col2" >0.00002%</td>
      <td id="T_052c9_row17_col3" class="data row17 col3" >0.00043%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row18" class="row_heading level0 row18" >XoRoShiRo1024**</th>
      <td id="T_052c9_row18_col0" class="data row18 col0" >0.00049%</td>
      <td id="T_052c9_row18_col1" class="data row18 col1" >0.00045%</td>
      <td id="T_052c9_row18_col2" class="data row18 col2" >0.00016%</td>
      <td id="T_052c9_row18_col3" class="data row18 col3" >0.00029%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row19" class="row_heading level0 row19" >L32X64Mix</th>
      <td id="T_052c9_row19_col0" class="data row19 col0" >0.00125%</td>
      <td id="T_052c9_row19_col1" class="data row19 col1" >0.00041%</td>
      <td id="T_052c9_row19_col2" class="data row19 col2" >0.00004%</td>
      <td id="T_052c9_row19_col3" class="data row19 col3" >0.00075%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row20" class="row_heading level0 row20" >L64X128Mix</th>
      <td id="T_052c9_row20_col0" class="data row20 col0" >0.00043%</td>
      <td id="T_052c9_row20_col1" class="data row20 col1" >0.00022%</td>
      <td id="T_052c9_row20_col2" class="data row20 col2" >0.00024%</td>
      <td id="T_052c9_row20_col3" class="data row20 col3" >0.00007%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row21" class="row_heading level0 row21" >L64X128**</th>
      <td id="T_052c9_row21_col0" class="data row21 col0" >0.00174%</td>
      <td id="T_052c9_row21_col1" class="data row21 col1" >0.00004%</td>
      <td id="T_052c9_row21_col2" class="data row21 col2" >0.00035%</td>
      <td id="T_052c9_row21_col3" class="data row21 col3" >0.00027%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row22" class="row_heading level0 row22" >L64X256Mix</th>
      <td id="T_052c9_row22_col0" class="data row22 col0" >0.00111%</td>
      <td id="T_052c9_row22_col1" class="data row22 col1" >0.00041%</td>
      <td id="T_052c9_row22_col2" class="data row22 col2" >0.00011%</td>
      <td id="T_052c9_row22_col3" class="data row22 col3" >0.00044%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row23" class="row_heading level0 row23" >L64X1024Mix</th>
      <td id="T_052c9_row23_col0" class="data row23 col0" >0.00227%</td>
      <td id="T_052c9_row23_col1" class="data row23 col1" >0.00050%</td>
      <td id="T_052c9_row23_col2" class="data row23 col2" >0.00052%</td>
      <td id="T_052c9_row23_col3" class="data row23 col3" >0.00015%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row24" class="row_heading level0 row24" >L128X128Mix</th>
      <td id="T_052c9_row24_col0" class="data row24 col0" >0.00176%</td>
      <td id="T_052c9_row24_col1" class="data row24 col1" >0.00004%</td>
      <td id="T_052c9_row24_col2" class="data row24 col2" >0.00021%</td>
      <td id="T_052c9_row24_col3" class="data row24 col3" >0.00027%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row25" class="row_heading level0 row25" >L128X256Mix</th>
      <td id="T_052c9_row25_col0" class="data row25 col0" >0.00001%</td>
      <td id="T_052c9_row25_col1" class="data row25 col1" >0.00047%</td>
      <td id="T_052c9_row25_col2" class="data row25 col2" >0.00016%</td>
      <td id="T_052c9_row25_col3" class="data row25 col3" >0.00018%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row26" class="row_heading level0 row26" >L128X1024Mix</th>
      <td id="T_052c9_row26_col0" class="data row26 col0" >0.00015%</td>
      <td id="T_052c9_row26_col1" class="data row26 col1" >0.00001%</td>
      <td id="T_052c9_row26_col2" class="data row26 col2" >0.00030%</td>
      <td id="T_052c9_row26_col3" class="data row26 col3" >0.00002%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row27" class="row_heading level0 row27" >PcgRxsMXs64</th>
      <td id="T_052c9_row27_col0" class="data row27 col0" >0.00156%</td>
      <td id="T_052c9_row27_col1" class="data row27 col1" >0.00055%</td>
      <td id="T_052c9_row27_col2" class="data row27 col2" >0.00033%</td>
      <td id="T_052c9_row27_col3" class="data row27 col3" >0.00030%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row28" class="row_heading level0 row28" >Philox4x64</th>
      <td id="T_052c9_row28_col0" class="data row28 col0" >0.00057%</td>
      <td id="T_052c9_row28_col1" class="data row28 col1" >0.00007%</td>
      <td id="T_052c9_row28_col2" class="data row28 col2" >0.00010%</td>
      <td id="T_052c9_row28_col3" class="data row28 col3" >0.00012%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row29" class="row_heading level0 row29" >Drand48</th>
      <td id="T_052c9_row29_col0" class="data row29 col0" >0.00060%</td>
      <td id="T_052c9_row29_col1" class="data row29 col1" >0.00027%</td>
      <td id="T_052c9_row29_col2" class="data row29 col2" >0.00134%</td>
      <td id="T_052c9_row29_col3" class="data row29 col3" >0.00046%</td>
    </tr>
    <tr>
      <th id="T_052c9_level0_row30" class="row_heading level0 row30" >Drand48Mix</th>
      <td id="T_052c9_row30_col0" class="data row30 col0" >0.00388%</td>
      <td id="T_052c9_row30_col1" class="data row30 col1" >0.00033%</td>
      <td id="T_052c9_row30_col2" class="data row30 col2" >0.00065%</td>
      <td id="T_052c9_row30_col3" class="data row30 col3" >0.00123%</td>
    </tr>
  </tbody>
</table>

### Standard deviation of the generated PRN

<table id="T_e9144">
  <caption>Standard Deviation Error (in %)</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_e9144_level0_col0" class="col_heading level0 col0" >Exponential</th>
      <th id="T_e9144_level0_col1" class="col_heading level0 col1" >Logarithmic</th>
      <th id="T_e9144_level0_col2" class="col_heading level0 col2" >Gamma</th>
      <th id="T_e9144_level0_col3" class="col_heading level0 col3" >Triangular</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_e9144_level0_row0" class="row_heading level0 row0" >ThreadLocalRandom</th>
      <td id="T_e9144_row0_col0" class="data row0 col0" >0.000%</td>
      <td id="T_e9144_row0_col1" class="data row0 col1" >0.001%</td>
      <td id="T_e9144_row0_col2" class="data row0 col2" >0.000%</td>
      <td id="T_e9144_row0_col3" class="data row0 col3" >0.001%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row1" class="row_heading level0 row1" >Random</th>
      <td id="T_e9144_row1_col0" class="data row1 col0" >0.001%</td>
      <td id="T_e9144_row1_col1" class="data row1 col1" >0.000%</td>
      <td id="T_e9144_row1_col2" class="data row1 col2" >0.002%</td>
      <td id="T_e9144_row1_col3" class="data row1 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row2" class="row_heading level0 row2" >SecureRandom</th>
      <td id="T_e9144_row2_col0" class="data row2 col0" >0.001%</td>
      <td id="T_e9144_row2_col1" class="data row2 col1" >0.004%</td>
      <td id="T_e9144_row2_col2" class="data row2 col2" >0.001%</td>
      <td id="T_e9144_row2_col3" class="data row2 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row3" class="row_heading level0 row3" >Well512a</th>
      <td id="T_e9144_row3_col0" class="data row3 col0" >0.000%</td>
      <td id="T_e9144_row3_col1" class="data row3 col1" >0.001%</td>
      <td id="T_e9144_row3_col2" class="data row3 col2" >0.003%</td>
      <td id="T_e9144_row3_col3" class="data row3 col3" >0.003%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row4" class="row_heading level0 row4" >Well1024a</th>
      <td id="T_e9144_row4_col0" class="data row4 col0" >0.002%</td>
      <td id="T_e9144_row4_col1" class="data row4 col1" >0.003%</td>
      <td id="T_e9144_row4_col2" class="data row4 col2" >0.001%</td>
      <td id="T_e9144_row4_col3" class="data row4 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row5" class="row_heading level0 row5" >Well19937a</th>
      <td id="T_e9144_row5_col0" class="data row5 col0" >0.000%</td>
      <td id="T_e9144_row5_col1" class="data row5 col1" >0.002%</td>
      <td id="T_e9144_row5_col2" class="data row5 col2" >0.001%</td>
      <td id="T_e9144_row5_col3" class="data row5 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row6" class="row_heading level0 row6" >Well19937c</th>
      <td id="T_e9144_row6_col0" class="data row6 col0" >0.002%</td>
      <td id="T_e9144_row6_col1" class="data row6 col1" >0.000%</td>
      <td id="T_e9144_row6_col2" class="data row6 col2" >0.000%</td>
      <td id="T_e9144_row6_col3" class="data row6 col3" >0.001%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row7" class="row_heading level0 row7" >Well44497a</th>
      <td id="T_e9144_row7_col0" class="data row7 col0" >0.002%</td>
      <td id="T_e9144_row7_col1" class="data row7 col1" >0.004%</td>
      <td id="T_e9144_row7_col2" class="data row7 col2" >0.001%</td>
      <td id="T_e9144_row7_col3" class="data row7 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row8" class="row_heading level0 row8" >Well44497b</th>
      <td id="T_e9144_row8_col0" class="data row8 col0" >0.002%</td>
      <td id="T_e9144_row8_col1" class="data row8 col1" >0.002%</td>
      <td id="T_e9144_row8_col2" class="data row8 col2" >0.002%</td>
      <td id="T_e9144_row8_col3" class="data row8 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row9" class="row_heading level0 row9" >MersenneTwister</th>
      <td id="T_e9144_row9_col0" class="data row9 col0" >0.000%</td>
      <td id="T_e9144_row9_col1" class="data row9 col1" >0.003%</td>
      <td id="T_e9144_row9_col2" class="data row9 col2" >0.003%</td>
      <td id="T_e9144_row9_col3" class="data row9 col3" >0.003%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row10" class="row_heading level0 row10" >SFC64</th>
      <td id="T_e9144_row10_col0" class="data row10 col0" >0.001%</td>
      <td id="T_e9144_row10_col1" class="data row10 col1" >0.002%</td>
      <td id="T_e9144_row10_col2" class="data row10 col2" >0.004%</td>
      <td id="T_e9144_row10_col3" class="data row10 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row11" class="row_heading level0 row11" >ISAAC</th>
      <td id="T_e9144_row11_col0" class="data row11 col0" >0.001%</td>
      <td id="T_e9144_row11_col1" class="data row11 col1" >0.001%</td>
      <td id="T_e9144_row11_col2" class="data row11 col2" >0.002%</td>
      <td id="T_e9144_row11_col3" class="data row11 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row12" class="row_heading level0 row12" >XoRoShiRo128++</th>
      <td id="T_e9144_row12_col0" class="data row12 col0" >0.001%</td>
      <td id="T_e9144_row12_col1" class="data row12 col1" >0.001%</td>
      <td id="T_e9144_row12_col2" class="data row12 col2" >0.003%</td>
      <td id="T_e9144_row12_col3" class="data row12 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row13" class="row_heading level0 row13" >XoRoShiRo128**</th>
      <td id="T_e9144_row13_col0" class="data row13 col0" >0.000%</td>
      <td id="T_e9144_row13_col1" class="data row13 col1" >0.001%</td>
      <td id="T_e9144_row13_col2" class="data row13 col2" >0.002%</td>
      <td id="T_e9144_row13_col3" class="data row13 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row14" class="row_heading level0 row14" >XoRoShiRo64**</th>
      <td id="T_e9144_row14_col0" class="data row14 col0" >0.002%</td>
      <td id="T_e9144_row14_col1" class="data row14 col1" >0.001%</td>
      <td id="T_e9144_row14_col2" class="data row14 col2" >0.001%</td>
      <td id="T_e9144_row14_col3" class="data row14 col3" >0.001%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row15" class="row_heading level0 row15" >XoRoShiRo256++</th>
      <td id="T_e9144_row15_col0" class="data row15 col0" >0.001%</td>
      <td id="T_e9144_row15_col1" class="data row15 col1" >0.002%</td>
      <td id="T_e9144_row15_col2" class="data row15 col2" >0.004%</td>
      <td id="T_e9144_row15_col3" class="data row15 col3" >0.001%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row16" class="row_heading level0 row16" >XoRoShiRo1024++</th>
      <td id="T_e9144_row16_col0" class="data row16 col0" >0.002%</td>
      <td id="T_e9144_row16_col1" class="data row16 col1" >0.002%</td>
      <td id="T_e9144_row16_col2" class="data row16 col2" >0.002%</td>
      <td id="T_e9144_row16_col3" class="data row16 col3" >0.001%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row17" class="row_heading level0 row17" >XoRoShiRo1024*</th>
      <td id="T_e9144_row17_col0" class="data row17 col0" >0.001%</td>
      <td id="T_e9144_row17_col1" class="data row17 col1" >0.002%</td>
      <td id="T_e9144_row17_col2" class="data row17 col2" >0.001%</td>
      <td id="T_e9144_row17_col3" class="data row17 col3" >0.000%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row18" class="row_heading level0 row18" >XoRoShiRo1024**</th>
      <td id="T_e9144_row18_col0" class="data row18 col0" >0.000%</td>
      <td id="T_e9144_row18_col1" class="data row18 col1" >0.002%</td>
      <td id="T_e9144_row18_col2" class="data row18 col2" >0.002%</td>
      <td id="T_e9144_row18_col3" class="data row18 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row19" class="row_heading level0 row19" >L32X64Mix</th>
      <td id="T_e9144_row19_col0" class="data row19 col0" >0.002%</td>
      <td id="T_e9144_row19_col1" class="data row19 col1" >0.002%</td>
      <td id="T_e9144_row19_col2" class="data row19 col2" >0.001%</td>
      <td id="T_e9144_row19_col3" class="data row19 col3" >0.001%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row20" class="row_heading level0 row20" >L64X128Mix</th>
      <td id="T_e9144_row20_col0" class="data row20 col0" >0.000%</td>
      <td id="T_e9144_row20_col1" class="data row20 col1" >0.001%</td>
      <td id="T_e9144_row20_col2" class="data row20 col2" >0.002%</td>
      <td id="T_e9144_row20_col3" class="data row20 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row21" class="row_heading level0 row21" >L64X128**</th>
      <td id="T_e9144_row21_col0" class="data row21 col0" >0.000%</td>
      <td id="T_e9144_row21_col1" class="data row21 col1" >0.001%</td>
      <td id="T_e9144_row21_col2" class="data row21 col2" >0.003%</td>
      <td id="T_e9144_row21_col3" class="data row21 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row22" class="row_heading level0 row22" >L64X256Mix</th>
      <td id="T_e9144_row22_col0" class="data row22 col0" >0.002%</td>
      <td id="T_e9144_row22_col1" class="data row22 col1" >0.002%</td>
      <td id="T_e9144_row22_col2" class="data row22 col2" >0.002%</td>
      <td id="T_e9144_row22_col3" class="data row22 col3" >0.001%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row23" class="row_heading level0 row23" >L64X1024Mix</th>
      <td id="T_e9144_row23_col0" class="data row23 col0" >0.001%</td>
      <td id="T_e9144_row23_col1" class="data row23 col1" >0.003%</td>
      <td id="T_e9144_row23_col2" class="data row23 col2" >0.002%</td>
      <td id="T_e9144_row23_col3" class="data row23 col3" >0.003%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row24" class="row_heading level0 row24" >L128X128Mix</th>
      <td id="T_e9144_row24_col0" class="data row24 col0" >0.001%</td>
      <td id="T_e9144_row24_col1" class="data row24 col1" >0.001%</td>
      <td id="T_e9144_row24_col2" class="data row24 col2" >0.001%</td>
      <td id="T_e9144_row24_col3" class="data row24 col3" >0.002%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row25" class="row_heading level0 row25" >L128X256Mix</th>
      <td id="T_e9144_row25_col0" class="data row25 col0" >0.000%</td>
      <td id="T_e9144_row25_col1" class="data row25 col1" >0.003%</td>
      <td id="T_e9144_row25_col2" class="data row25 col2" >0.001%</td>
      <td id="T_e9144_row25_col3" class="data row25 col3" >0.001%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row26" class="row_heading level0 row26" >L128X1024Mix</th>
      <td id="T_e9144_row26_col0" class="data row26 col0" >0.001%</td>
      <td id="T_e9144_row26_col1" class="data row26 col1" >0.002%</td>
      <td id="T_e9144_row26_col2" class="data row26 col2" >0.002%</td>
      <td id="T_e9144_row26_col3" class="data row26 col3" >0.003%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row27" class="row_heading level0 row27" >PcgRxsMXs64</th>
      <td id="T_e9144_row27_col0" class="data row27 col0" >0.001%</td>
      <td id="T_e9144_row27_col1" class="data row27 col1" >0.001%</td>
      <td id="T_e9144_row27_col2" class="data row27 col2" >0.001%</td>
      <td id="T_e9144_row27_col3" class="data row27 col3" >0.003%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row28" class="row_heading level0 row28" >Philox4x64</th>
      <td id="T_e9144_row28_col0" class="data row28 col0" >0.001%</td>
      <td id="T_e9144_row28_col1" class="data row28 col1" >0.003%</td>
      <td id="T_e9144_row28_col2" class="data row28 col2" >0.001%</td>
      <td id="T_e9144_row28_col3" class="data row28 col3" >0.001%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row29" class="row_heading level0 row29" >Drand48</th>
      <td id="T_e9144_row29_col0" class="data row29 col0" >0.008%</td>
      <td id="T_e9144_row29_col1" class="data row29 col1" >0.003%</td>
      <td id="T_e9144_row29_col2" class="data row29 col2" >0.008%</td>
      <td id="T_e9144_row29_col3" class="data row29 col3" >0.004%</td>
    </tr>
    <tr>
      <th id="T_e9144_level0_row30" class="row_heading level0 row30" >Drand48Mix</th>
      <td id="T_e9144_row30_col0" class="data row30 col0" >0.009%</td>
      <td id="T_e9144_row30_col1" class="data row30 col1" >0.008%</td>
      <td id="T_e9144_row30_col2" class="data row30 col2" >0.005%</td>
      <td id="T_e9144_row30_col3" class="data row30 col3" >0.009%</td>
    </tr>
  </tbody>
</table>

### Comparison of theoretical PDF and histogram of the PRN

<table id="T_42bb6">
  <caption>&Delta;<sup>2</sup></caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_42bb6_level0_col0" class="col_heading level0 col0" >Exponential</th>
      <th id="T_42bb6_level0_col1" class="col_heading level0 col1" >Logarithmic</th>
      <th id="T_42bb6_level0_col2" class="col_heading level0 col2" >Gamma</th>
      <th id="T_42bb6_level0_col3" class="col_heading level0 col3" >Triangular</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_42bb6_level0_row0" class="row_heading level0 row0" >ThreadLocalRandom</th>
      <td id="T_42bb6_row0_col0" class="data row0 col0" >1.00</td>
      <td id="T_42bb6_row0_col1" class="data row0 col1" >1.00</td>
      <td id="T_42bb6_row0_col2" class="data row0 col2" >0.99</td>
      <td id="T_42bb6_row0_col3" class="data row0 col3" >1.00</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row1" class="row_heading level0 row1" >Random</th>
      <td id="T_42bb6_row1_col0" class="data row1 col0" >1.01</td>
      <td id="T_42bb6_row1_col1" class="data row1 col1" >0.99</td>
      <td id="T_42bb6_row1_col2" class="data row1 col2" >0.99</td>
      <td id="T_42bb6_row1_col3" class="data row1 col3" >0.98</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row2" class="row_heading level0 row2" >SecureRandom</th>
      <td id="T_42bb6_row2_col0" class="data row2 col0" >0.99</td>
      <td id="T_42bb6_row2_col1" class="data row2 col1" >0.99</td>
      <td id="T_42bb6_row2_col2" class="data row2 col2" >1.01</td>
      <td id="T_42bb6_row2_col3" class="data row2 col3" >1.00</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row3" class="row_heading level0 row3" >Well512a</th>
      <td id="T_42bb6_row3_col0" class="data row3 col0" >0.99</td>
      <td id="T_42bb6_row3_col1" class="data row3 col1" >0.98</td>
      <td id="T_42bb6_row3_col2" class="data row3 col2" >1.00</td>
      <td id="T_42bb6_row3_col3" class="data row3 col3" >0.99</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row4" class="row_heading level0 row4" >Well1024a</th>
      <td id="T_42bb6_row4_col0" class="data row4 col0" >1.00</td>
      <td id="T_42bb6_row4_col1" class="data row4 col1" >0.98</td>
      <td id="T_42bb6_row4_col2" class="data row4 col2" >1.01</td>
      <td id="T_42bb6_row4_col3" class="data row4 col3" >1.00</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row5" class="row_heading level0 row5" >Well19937a</th>
      <td id="T_42bb6_row5_col0" class="data row5 col0" >1.00</td>
      <td id="T_42bb6_row5_col1" class="data row5 col1" >1.00</td>
      <td id="T_42bb6_row5_col2" class="data row5 col2" >1.00</td>
      <td id="T_42bb6_row5_col3" class="data row5 col3" >0.99</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row6" class="row_heading level0 row6" >Well19937c</th>
      <td id="T_42bb6_row6_col0" class="data row6 col0" >1.01</td>
      <td id="T_42bb6_row6_col1" class="data row6 col1" >0.98</td>
      <td id="T_42bb6_row6_col2" class="data row6 col2" >1.00</td>
      <td id="T_42bb6_row6_col3" class="data row6 col3" >0.99</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row7" class="row_heading level0 row7" >Well44497a</th>
      <td id="T_42bb6_row7_col0" class="data row7 col0" >0.99</td>
      <td id="T_42bb6_row7_col1" class="data row7 col1" >1.00</td>
      <td id="T_42bb6_row7_col2" class="data row7 col2" >0.99</td>
      <td id="T_42bb6_row7_col3" class="data row7 col3" >1.00</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row8" class="row_heading level0 row8" >Well44497b</th>
      <td id="T_42bb6_row8_col0" class="data row8 col0" >1.00</td>
      <td id="T_42bb6_row8_col1" class="data row8 col1" >1.00</td>
      <td id="T_42bb6_row8_col2" class="data row8 col2" >1.00</td>
      <td id="T_42bb6_row8_col3" class="data row8 col3" >1.02</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row9" class="row_heading level0 row9" >MersenneTwister</th>
      <td id="T_42bb6_row9_col0" class="data row9 col0" >1.01</td>
      <td id="T_42bb6_row9_col1" class="data row9 col1" >0.99</td>
      <td id="T_42bb6_row9_col2" class="data row9 col2" >0.98</td>
      <td id="T_42bb6_row9_col3" class="data row9 col3" >0.99</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row10" class="row_heading level0 row10" >SFC64</th>
      <td id="T_42bb6_row10_col0" class="data row10 col0" >1.04</td>
      <td id="T_42bb6_row10_col1" class="data row10 col1" >1.04</td>
      <td id="T_42bb6_row10_col2" class="data row10 col2" >1.02</td>
      <td id="T_42bb6_row10_col3" class="data row10 col3" >1.14</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row11" class="row_heading level0 row11" >ISAAC</th>
      <td id="T_42bb6_row11_col0" class="data row11 col0" >0.99</td>
      <td id="T_42bb6_row11_col1" class="data row11 col1" >0.97</td>
      <td id="T_42bb6_row11_col2" class="data row11 col2" >0.99</td>
      <td id="T_42bb6_row11_col3" class="data row11 col3" >0.98</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row12" class="row_heading level0 row12" >XoRoShiRo128++</th>
      <td id="T_42bb6_row12_col0" class="data row12 col0" >1.02</td>
      <td id="T_42bb6_row12_col1" class="data row12 col1" >1.03</td>
      <td id="T_42bb6_row12_col2" class="data row12 col2" >1.03</td>
      <td id="T_42bb6_row12_col3" class="data row12 col3" >1.05</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row13" class="row_heading level0 row13" >XoRoShiRo128**</th>
      <td id="T_42bb6_row13_col0" class="data row13 col0" >1.03</td>
      <td id="T_42bb6_row13_col1" class="data row13 col1" >1.02</td>
      <td id="T_42bb6_row13_col2" class="data row13 col2" >1.01</td>
      <td id="T_42bb6_row13_col3" class="data row13 col3" >1.01</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row14" class="row_heading level0 row14" >XoRoShiRo64**</th>
      <td id="T_42bb6_row14_col0" class="data row14 col0" >1.03</td>
      <td id="T_42bb6_row14_col1" class="data row14 col1" >1.03</td>
      <td id="T_42bb6_row14_col2" class="data row14 col2" >1.03</td>
      <td id="T_42bb6_row14_col3" class="data row14 col3" >1.04</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row15" class="row_heading level0 row15" >XoRoShiRo256++</th>
      <td id="T_42bb6_row15_col0" class="data row15 col0" >1.00</td>
      <td id="T_42bb6_row15_col1" class="data row15 col1" >0.99</td>
      <td id="T_42bb6_row15_col2" class="data row15 col2" >1.00</td>
      <td id="T_42bb6_row15_col3" class="data row15 col3" >1.00</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row16" class="row_heading level0 row16" >XoRoShiRo1024++</th>
      <td id="T_42bb6_row16_col0" class="data row16 col0" >1.00</td>
      <td id="T_42bb6_row16_col1" class="data row16 col1" >1.01</td>
      <td id="T_42bb6_row16_col2" class="data row16 col2" >1.01</td>
      <td id="T_42bb6_row16_col3" class="data row16 col3" >1.07</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row17" class="row_heading level0 row17" >XoRoShiRo1024*</th>
      <td id="T_42bb6_row17_col0" class="data row17 col0" >1.03</td>
      <td id="T_42bb6_row17_col1" class="data row17 col1" >1.01</td>
      <td id="T_42bb6_row17_col2" class="data row17 col2" >1.02</td>
      <td id="T_42bb6_row17_col3" class="data row17 col3" >1.06</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row18" class="row_heading level0 row18" >XoRoShiRo1024**</th>
      <td id="T_42bb6_row18_col0" class="data row18 col0" >1.02</td>
      <td id="T_42bb6_row18_col1" class="data row18 col1" >1.02</td>
      <td id="T_42bb6_row18_col2" class="data row18 col2" >1.03</td>
      <td id="T_42bb6_row18_col3" class="data row18 col3" >1.06</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row19" class="row_heading level0 row19" >L32X64Mix</th>
      <td id="T_42bb6_row19_col0" class="data row19 col0" >1.03</td>
      <td id="T_42bb6_row19_col1" class="data row19 col1" >1.01</td>
      <td id="T_42bb6_row19_col2" class="data row19 col2" >1.01</td>
      <td id="T_42bb6_row19_col3" class="data row19 col3" >1.01</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row20" class="row_heading level0 row20" >L64X128Mix</th>
      <td id="T_42bb6_row20_col0" class="data row20 col0" >1.00</td>
      <td id="T_42bb6_row20_col1" class="data row20 col1" >1.00</td>
      <td id="T_42bb6_row20_col2" class="data row20 col2" >1.00</td>
      <td id="T_42bb6_row20_col3" class="data row20 col3" >0.97</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row21" class="row_heading level0 row21" >L64X128**</th>
      <td id="T_42bb6_row21_col0" class="data row21 col0" >1.00</td>
      <td id="T_42bb6_row21_col1" class="data row21 col1" >1.00</td>
      <td id="T_42bb6_row21_col2" class="data row21 col2" >1.00</td>
      <td id="T_42bb6_row21_col3" class="data row21 col3" >1.00</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row22" class="row_heading level0 row22" >L64X256Mix</th>
      <td id="T_42bb6_row22_col0" class="data row22 col0" >1.00</td>
      <td id="T_42bb6_row22_col1" class="data row22 col1" >1.00</td>
      <td id="T_42bb6_row22_col2" class="data row22 col2" >0.98</td>
      <td id="T_42bb6_row22_col3" class="data row22 col3" >1.00</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row23" class="row_heading level0 row23" >L64X1024Mix</th>
      <td id="T_42bb6_row23_col0" class="data row23 col0" >0.99</td>
      <td id="T_42bb6_row23_col1" class="data row23 col1" >1.00</td>
      <td id="T_42bb6_row23_col2" class="data row23 col2" >0.99</td>
      <td id="T_42bb6_row23_col3" class="data row23 col3" >0.99</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row24" class="row_heading level0 row24" >L128X128Mix</th>
      <td id="T_42bb6_row24_col0" class="data row24 col0" >0.99</td>
      <td id="T_42bb6_row24_col1" class="data row24 col1" >1.00</td>
      <td id="T_42bb6_row24_col2" class="data row24 col2" >0.99</td>
      <td id="T_42bb6_row24_col3" class="data row24 col3" >1.01</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row25" class="row_heading level0 row25" >L128X256Mix</th>
      <td id="T_42bb6_row25_col0" class="data row25 col0" >0.99</td>
      <td id="T_42bb6_row25_col1" class="data row25 col1" >0.99</td>
      <td id="T_42bb6_row25_col2" class="data row25 col2" >1.00</td>
      <td id="T_42bb6_row25_col3" class="data row25 col3" >0.98</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row26" class="row_heading level0 row26" >L128X1024Mix</th>
      <td id="T_42bb6_row26_col0" class="data row26 col0" >1.00</td>
      <td id="T_42bb6_row26_col1" class="data row26 col1" >0.98</td>
      <td id="T_42bb6_row26_col2" class="data row26 col2" >0.99</td>
      <td id="T_42bb6_row26_col3" class="data row26 col3" >1.01</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row27" class="row_heading level0 row27" >PcgRxsMXs64</th>
      <td id="T_42bb6_row27_col0" class="data row27 col0" >1.05</td>
      <td id="T_42bb6_row27_col1" class="data row27 col1" >1.03</td>
      <td id="T_42bb6_row27_col2" class="data row27 col2" >1.04</td>
      <td id="T_42bb6_row27_col3" class="data row27 col3" >1.04</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row28" class="row_heading level0 row28" >Philox4x64</th>
      <td id="T_42bb6_row28_col0" class="data row28 col0" >1.02</td>
      <td id="T_42bb6_row28_col1" class="data row28 col1" >1.03</td>
      <td id="T_42bb6_row28_col2" class="data row28 col2" >0.99</td>
      <td id="T_42bb6_row28_col3" class="data row28 col3" >1.06</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row29" class="row_heading level0 row29" >Drand48</th>
      <td id="T_42bb6_row29_col0" class="data row29 col0" >16.56</td>
      <td id="T_42bb6_row29_col1" class="data row29 col1" >18.52</td>
      <td id="T_42bb6_row29_col2" class="data row29 col2" >16.46</td>
      <td id="T_42bb6_row29_col3" class="data row29 col3" >17.57</td>
    </tr>
    <tr>
      <th id="T_42bb6_level0_row30" class="row_heading level0 row30" >Drand48Mix</th>
      <td id="T_42bb6_row30_col0" class="data row30 col0" >19.47</td>
      <td id="T_42bb6_row30_col1" class="data row30 col1" >20.13</td>
      <td id="T_42bb6_row30_col2" class="data row30 col2" >20.37</td>
      <td id="T_42bb6_row30_col3" class="data row30 col3" >19.23</td>
    </tr>
  </tbody>
</table>

## Comparison boxplot for exponential distribution

![Boxplots of the relative errors of the different pseudorandom number generators](plot1boxplots-Exp.png)

## Comparison boxplot for log-normal distribution

![Boxplots of the relative errors of the different pseudorandom number generators](plot1boxplots-LogNormal.png)

## Comparison boxplot for gamma distribution

![Boxplots of the relative errors of the different pseudorandom number generators](plot1boxplots-Gamma.png)

## Comparison boxplot for triangular distribution

![Boxplots of the relative errors of the different pseudorandom number generators](plot1boxplots-Triangular.png)

## Times needed to generate the PRN

<table id="T_c0d70">
  <caption>Times to generate PRN (Normalized to fastest in each column)</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_c0d70_level0_col0" class="col_heading level0 col0" >Exponential</th>
      <th id="T_c0d70_level0_col1" class="col_heading level0 col1" >Logarithmic</th>
      <th id="T_c0d70_level0_col2" class="col_heading level0 col2" >Gamma</th>
      <th id="T_c0d70_level0_col3" class="col_heading level0 col3" >Triangular</th>
      <th id="T_c0d70_level0_col4" class="col_heading level0 col4" >Average</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c0d70_level0_row0" class="row_heading level0 row0" >ThreadLocalRandom</th>
      <td id="T_c0d70_row0_col0" class="data row0 col0" >107%</td>
      <td id="T_c0d70_row0_col1" class="data row0 col1" >100%</td>
      <td id="T_c0d70_row0_col2" class="data row0 col2" >100%</td>
      <td id="T_c0d70_row0_col3" class="data row0 col3" >107%</td>
      <td id="T_c0d70_row0_col4" class="data row0 col4" >101%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row1" class="row_heading level0 row1" >Random</th>
      <td id="T_c0d70_row1_col0" class="data row1 col0" >108%</td>
      <td id="T_c0d70_row1_col1" class="data row1 col1" >102%</td>
      <td id="T_c0d70_row1_col2" class="data row1 col2" >104%</td>
      <td id="T_c0d70_row1_col3" class="data row1 col3" >107%</td>
      <td id="T_c0d70_row1_col4" class="data row1 col4" >103%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row2" class="row_heading level0 row2" >SecureRandom</th>
      <td id="T_c0d70_row2_col0" class="data row2 col0" >377%</td>
      <td id="T_c0d70_row2_col1" class="data row2 col1" >412%</td>
      <td id="T_c0d70_row2_col2" class="data row2 col2" >650%</td>
      <td id="T_c0d70_row2_col3" class="data row2 col3" >370%</td>
      <td id="T_c0d70_row2_col4" class="data row2 col4" >447%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row3" class="row_heading level0 row3" >Well512a</th>
      <td id="T_c0d70_row3_col0" class="data row3 col0" >109%</td>
      <td id="T_c0d70_row3_col1" class="data row3 col1" >109%</td>
      <td id="T_c0d70_row3_col2" class="data row3 col2" >117%</td>
      <td id="T_c0d70_row3_col3" class="data row3 col3" >113%</td>
      <td id="T_c0d70_row3_col4" class="data row3 col4" >110%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row4" class="row_heading level0 row4" >Well1024a</th>
      <td id="T_c0d70_row4_col0" class="data row4 col0" >109%</td>
      <td id="T_c0d70_row4_col1" class="data row4 col1" >107%</td>
      <td id="T_c0d70_row4_col2" class="data row4 col2" >117%</td>
      <td id="T_c0d70_row4_col3" class="data row4 col3" >114%</td>
      <td id="T_c0d70_row4_col4" class="data row4 col4" >110%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row5" class="row_heading level0 row5" >Well19937a</th>
      <td id="T_c0d70_row5_col0" class="data row5 col0" >110%</td>
      <td id="T_c0d70_row5_col1" class="data row5 col1" >113%</td>
      <td id="T_c0d70_row5_col2" class="data row5 col2" >123%</td>
      <td id="T_c0d70_row5_col3" class="data row5 col3" >117%</td>
      <td id="T_c0d70_row5_col4" class="data row5 col4" >114%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row6" class="row_heading level0 row6" >Well19937c</th>
      <td id="T_c0d70_row6_col0" class="data row6 col0" >111%</td>
      <td id="T_c0d70_row6_col1" class="data row6 col1" >112%</td>
      <td id="T_c0d70_row6_col2" class="data row6 col2" >127%</td>
      <td id="T_c0d70_row6_col3" class="data row6 col3" >117%</td>
      <td id="T_c0d70_row6_col4" class="data row6 col4" >115%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row7" class="row_heading level0 row7" >Well44497a</th>
      <td id="T_c0d70_row7_col0" class="data row7 col0" >111%</td>
      <td id="T_c0d70_row7_col1" class="data row7 col1" >114%</td>
      <td id="T_c0d70_row7_col2" class="data row7 col2" >125%</td>
      <td id="T_c0d70_row7_col3" class="data row7 col3" >116%</td>
      <td id="T_c0d70_row7_col4" class="data row7 col4" >114%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row8" class="row_heading level0 row8" >Well44497b</th>
      <td id="T_c0d70_row8_col0" class="data row8 col0" >113%</td>
      <td id="T_c0d70_row8_col1" class="data row8 col1" >113%</td>
      <td id="T_c0d70_row8_col2" class="data row8 col2" >127%</td>
      <td id="T_c0d70_row8_col3" class="data row8 col3" >116%</td>
      <td id="T_c0d70_row8_col4" class="data row8 col4" >115%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row9" class="row_heading level0 row9" >MersenneTwister</th>
      <td id="T_c0d70_row9_col0" class="data row9 col0" >108%</td>
      <td id="T_c0d70_row9_col1" class="data row9 col1" >109%</td>
      <td id="T_c0d70_row9_col2" class="data row9 col2" >119%</td>
      <td id="T_c0d70_row9_col3" class="data row9 col3" >111%</td>
      <td id="T_c0d70_row9_col4" class="data row9 col4" >110%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row10" class="row_heading level0 row10" >SFC64</th>
      <td id="T_c0d70_row10_col0" class="data row10 col0" >100%</td>
      <td id="T_c0d70_row10_col1" class="data row10 col1" >104%</td>
      <td id="T_c0d70_row10_col2" class="data row10 col2" >103%</td>
      <td id="T_c0d70_row10_col3" class="data row10 col3" >100%</td>
      <td id="T_c0d70_row10_col4" class="data row10 col4" >100%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row11" class="row_heading level0 row11" >ISAAC</th>
      <td id="T_c0d70_row11_col0" class="data row11 col0" >109%</td>
      <td id="T_c0d70_row11_col1" class="data row11 col1" >108%</td>
      <td id="T_c0d70_row11_col2" class="data row11 col2" >122%</td>
      <td id="T_c0d70_row11_col3" class="data row11 col3" >113%</td>
      <td id="T_c0d70_row11_col4" class="data row11 col4" >111%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row12" class="row_heading level0 row12" >XoRoShiRo128++</th>
      <td id="T_c0d70_row12_col0" class="data row12 col0" >103%</td>
      <td id="T_c0d70_row12_col1" class="data row12 col1" >107%</td>
      <td id="T_c0d70_row12_col2" class="data row12 col2" >112%</td>
      <td id="T_c0d70_row12_col3" class="data row12 col3" >113%</td>
      <td id="T_c0d70_row12_col4" class="data row12 col4" >107%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row13" class="row_heading level0 row13" >XoRoShiRo128**</th>
      <td id="T_c0d70_row13_col0" class="data row13 col0" >101%</td>
      <td id="T_c0d70_row13_col1" class="data row13 col1" >104%</td>
      <td id="T_c0d70_row13_col2" class="data row13 col2" >113%</td>
      <td id="T_c0d70_row13_col3" class="data row13 col3" >110%</td>
      <td id="T_c0d70_row13_col4" class="data row13 col4" >106%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row14" class="row_heading level0 row14" >XoRoShiRo64**</th>
      <td id="T_c0d70_row14_col0" class="data row14 col0" >101%</td>
      <td id="T_c0d70_row14_col1" class="data row14 col1" >107%</td>
      <td id="T_c0d70_row14_col2" class="data row14 col2" >115%</td>
      <td id="T_c0d70_row14_col3" class="data row14 col3" >110%</td>
      <td id="T_c0d70_row14_col4" class="data row14 col4" >107%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row15" class="row_heading level0 row15" >XoRoShiRo256++</th>
      <td id="T_c0d70_row15_col0" class="data row15 col0" >117%</td>
      <td id="T_c0d70_row15_col1" class="data row15 col1" >121%</td>
      <td id="T_c0d70_row15_col2" class="data row15 col2" >122%</td>
      <td id="T_c0d70_row15_col3" class="data row15 col3" >122%</td>
      <td id="T_c0d70_row15_col4" class="data row15 col4" >118%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row16" class="row_heading level0 row16" >XoRoShiRo1024++</th>
      <td id="T_c0d70_row16_col0" class="data row16 col0" >104%</td>
      <td id="T_c0d70_row16_col1" class="data row16 col1" >109%</td>
      <td id="T_c0d70_row16_col2" class="data row16 col2" >107%</td>
      <td id="T_c0d70_row16_col3" class="data row16 col3" >104%</td>
      <td id="T_c0d70_row16_col4" class="data row16 col4" >104%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row17" class="row_heading level0 row17" >XoRoShiRo1024*</th>
      <td id="T_c0d70_row17_col0" class="data row17 col0" >107%</td>
      <td id="T_c0d70_row17_col1" class="data row17 col1" >109%</td>
      <td id="T_c0d70_row17_col2" class="data row17 col2" >108%</td>
      <td id="T_c0d70_row17_col3" class="data row17 col3" >105%</td>
      <td id="T_c0d70_row17_col4" class="data row17 col4" >106%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row18" class="row_heading level0 row18" >XoRoShiRo1024**</th>
      <td id="T_c0d70_row18_col0" class="data row18 col0" >108%</td>
      <td id="T_c0d70_row18_col1" class="data row18 col1" >110%</td>
      <td id="T_c0d70_row18_col2" class="data row18 col2" >109%</td>
      <td id="T_c0d70_row18_col3" class="data row18 col3" >106%</td>
      <td id="T_c0d70_row18_col4" class="data row18 col4" >106%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row19" class="row_heading level0 row19" >L32X64Mix</th>
      <td id="T_c0d70_row19_col0" class="data row19 col0" >105%</td>
      <td id="T_c0d70_row19_col1" class="data row19 col1" >105%</td>
      <td id="T_c0d70_row19_col2" class="data row19 col2" >114%</td>
      <td id="T_c0d70_row19_col3" class="data row19 col3" >110%</td>
      <td id="T_c0d70_row19_col4" class="data row19 col4" >106%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row20" class="row_heading level0 row20" >L64X128Mix</th>
      <td id="T_c0d70_row20_col0" class="data row20 col0" >119%</td>
      <td id="T_c0d70_row20_col1" class="data row20 col1" >123%</td>
      <td id="T_c0d70_row20_col2" class="data row20 col2" >124%</td>
      <td id="T_c0d70_row20_col3" class="data row20 col3" >123%</td>
      <td id="T_c0d70_row20_col4" class="data row20 col4" >120%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row21" class="row_heading level0 row21" >L64X128**</th>
      <td id="T_c0d70_row21_col0" class="data row21 col0" >123%</td>
      <td id="T_c0d70_row21_col1" class="data row21 col1" >122%</td>
      <td id="T_c0d70_row21_col2" class="data row21 col2" >126%</td>
      <td id="T_c0d70_row21_col3" class="data row21 col3" >122%</td>
      <td id="T_c0d70_row21_col4" class="data row21 col4" >121%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row22" class="row_heading level0 row22" >L64X256Mix</th>
      <td id="T_c0d70_row22_col0" class="data row22 col0" >125%</td>
      <td id="T_c0d70_row22_col1" class="data row22 col1" >123%</td>
      <td id="T_c0d70_row22_col2" class="data row22 col2" >127%</td>
      <td id="T_c0d70_row22_col3" class="data row22 col3" >123%</td>
      <td id="T_c0d70_row22_col4" class="data row22 col4" >122%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row23" class="row_heading level0 row23" >L64X1024Mix</th>
      <td id="T_c0d70_row23_col0" class="data row23 col0" >127%</td>
      <td id="T_c0d70_row23_col1" class="data row23 col1" >124%</td>
      <td id="T_c0d70_row23_col2" class="data row23 col2" >128%</td>
      <td id="T_c0d70_row23_col3" class="data row23 col3" >124%</td>
      <td id="T_c0d70_row23_col4" class="data row23 col4" >123%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row24" class="row_heading level0 row24" >L128X128Mix</th>
      <td id="T_c0d70_row24_col0" class="data row24 col0" >124%</td>
      <td id="T_c0d70_row24_col1" class="data row24 col1" >124%</td>
      <td id="T_c0d70_row24_col2" class="data row24 col2" >128%</td>
      <td id="T_c0d70_row24_col3" class="data row24 col3" >126%</td>
      <td id="T_c0d70_row24_col4" class="data row24 col4" >123%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row25" class="row_heading level0 row25" >L128X256Mix</th>
      <td id="T_c0d70_row25_col0" class="data row25 col0" >122%</td>
      <td id="T_c0d70_row25_col1" class="data row25 col1" >123%</td>
      <td id="T_c0d70_row25_col2" class="data row25 col2" >128%</td>
      <td id="T_c0d70_row25_col3" class="data row25 col3" >126%</td>
      <td id="T_c0d70_row25_col4" class="data row25 col4" >123%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row26" class="row_heading level0 row26" >L128X1024Mix</th>
      <td id="T_c0d70_row26_col0" class="data row26 col0" >124%</td>
      <td id="T_c0d70_row26_col1" class="data row26 col1" >124%</td>
      <td id="T_c0d70_row26_col2" class="data row26 col2" >129%</td>
      <td id="T_c0d70_row26_col3" class="data row26 col3" >126%</td>
      <td id="T_c0d70_row26_col4" class="data row26 col4" >123%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row27" class="row_heading level0 row27" >PcgRxsMXs64</th>
      <td id="T_c0d70_row27_col0" class="data row27 col0" >108%</td>
      <td id="T_c0d70_row27_col1" class="data row27 col1" >110%</td>
      <td id="T_c0d70_row27_col2" class="data row27 col2" >109%</td>
      <td id="T_c0d70_row27_col3" class="data row27 col3" >106%</td>
      <td id="T_c0d70_row27_col4" class="data row27 col4" >106%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row28" class="row_heading level0 row28" >Philox4x64</th>
      <td id="T_c0d70_row28_col0" class="data row28 col0" >110%</td>
      <td id="T_c0d70_row28_col1" class="data row28 col1" >114%</td>
      <td id="T_c0d70_row28_col2" class="data row28 col2" >111%</td>
      <td id="T_c0d70_row28_col3" class="data row28 col3" >108%</td>
      <td id="T_c0d70_row28_col4" class="data row28 col4" >109%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row29" class="row_heading level0 row29" >Drand48</th>
      <td id="T_c0d70_row29_col0" class="data row29 col0" >101%</td>
      <td id="T_c0d70_row29_col1" class="data row29 col1" >105%</td>
      <td id="T_c0d70_row29_col2" class="data row29 col2" >109%</td>
      <td id="T_c0d70_row29_col3" class="data row29 col3" >108%</td>
      <td id="T_c0d70_row29_col4" class="data row29 col4" >104%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row30" class="row_heading level0 row30" >Drand48Mix</th>
      <td id="T_c0d70_row30_col0" class="data row30 col0" >110%</td>
      <td id="T_c0d70_row30_col1" class="data row30 col1" >112%</td>
      <td id="T_c0d70_row30_col2" class="data row30 col2" >116%</td>
      <td id="T_c0d70_row30_col3" class="data row30 col3" >115%</td>
      <td id="T_c0d70_row30_col4" class="data row30 col4" >111%</td>
    </tr>
    <tr>
      <th id="T_c0d70_level0_row31" class="row_heading level0 row31" >ThreadLocalRandomSlow</th>
      <td id="T_c0d70_row31_col0" class="data row31 col0" >112%</td>
      <td id="T_c0d70_row31_col1" class="data row31 col1" >115%</td>
      <td id="T_c0d70_row31_col2" class="data row31 col2" >111%</td>
      <td id="T_c0d70_row31_col3" class="data row31 col3" >112%</td>
      <td id="T_c0d70_row31_col4" class="data row31 col4" >111%</td>
    </tr>
  </tbody>
</table>

(Values are column-wise normalized to the fasted generator, i.e. the fastest generator in each column has the value 100%.)

The generators XoRoShiRo256++, L64X128Mix, L64X128**, L64X256Mix, L64X1024Mix, L128X128Mix, L128X256Mix and L128X1024Mix are linked via reflection. Therefore they are a bit slower than the other generators of the same families.

## Autocorrelations

### Boxplots of the autocorrelation at lag 1 of the PRN of the different pseudorandom number generator

![Boxplots of the autocorrelation at lag 1 of the PRN of the different pseudorandom number generators](plot1autocorrelation1.png)

### Boxplots of the autocorrelation at lag 2 of the PRN of the different pseudorandom number generator

![Boxplots of the autocorrelation at lag 2 of the PRN of the different pseudorandom number generators](plot1autocorrelation2.png)

### Boxplots of the autocorrelation at lag 3 of the PRN of the different pseudorandom number generator

![Boxplots of the autocorrelation at lag 3 of the PRN of the different pseudorandom number generators](plot1autocorrelation3.png)

### Boxplots of the absolute sum of the autocorrelation at lags 1 to 100 of the PRN of the different pseudorandom number generators

![Boxplots of the absolute sum of the autocorrelation at lags 1 to 100 of the PRN of the different pseudorandom number generators](plot1autocorrelationSum.png)


## Raw result data

Raw data from the simulations as tabulator separated text files:

* [Exponential distribution](statistics/results1Exp.txt)
* [Log-normal distribution](statistics/results1Log.txt)
* [Gamma distribution](statistics/results1Gamma.txt)
* [Triangular distribution](statistics/results1Triangular.txt)

Raw data from the simulations for the autocorrelations as tabulator separated text files:

* [Exponential distribution](statistics/results1ExpAutokorrelation.txt)
* [Log-normal distribution](statistics/results1LogAutokorrelation.txt)
* [Gamma distribution](statistics/results1GammaAutokorrelation.txt)
* [Triangular distribution](statistics/results1TriangularAutokorrelation.txt)

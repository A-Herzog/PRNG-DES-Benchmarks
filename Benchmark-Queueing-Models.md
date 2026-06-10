# Queueing models

The following 31 pseudorandom numbers generators (PRNG) have been tested to generate pseudorandom numbers (PRN) for a M/M/1 and a M/G/1 queueing model each with an utilization of $\rho=90\,\%$ and $\rho=95\,\%$. In the M/G/1 case, the service time distribution is a log-normal distribution.

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
* SFC64
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

## Simulations results

### M/M/1 and M/G/1 - $\rho=90\,\%$

<table id="T_6ac90">
  <caption>Mean Error (in \%)</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_6ac90_level0_col0" class="col_heading level0 col0" >E[W] - MM1</th>
      <th id="T_6ac90_level0_col1" class="col_heading level0 col1" >E[V] - MM1</th>
      <th id="T_6ac90_level0_col2" class="col_heading level0 col2" >E[W] - MG1Log</th>
      <th id="T_6ac90_level0_col3" class="col_heading level0 col3" >E[V] - MG1Log</th>
      <th id="T_6ac90_level0_col4" class="col_heading level0 col4" >E[W] - MG1Gamma</th>
      <th id="T_6ac90_level0_col5" class="col_heading level0 col5" >E[V] - MG1Gamma</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_6ac90_level0_row0" class="row_heading level0 row0" >ThreadLocalRandom</th>
      <td id="T_6ac90_row0_col0" class="data row0 col0" >0.014%</td>
      <td id="T_6ac90_row0_col1" class="data row0 col1" >0.013%</td>
      <td id="T_6ac90_row0_col2" class="data row0 col2" >0.008%</td>
      <td id="T_6ac90_row0_col3" class="data row0 col3" >0.007%</td>
      <td id="T_6ac90_row0_col4" class="data row0 col4" >0.003%</td>
      <td id="T_6ac90_row0_col5" class="data row0 col5" >0.003%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row1" class="row_heading level0 row1" >Random</th>
      <td id="T_6ac90_row1_col0" class="data row1 col0" >0.021%</td>
      <td id="T_6ac90_row1_col1" class="data row1 col1" >0.019%</td>
      <td id="T_6ac90_row1_col2" class="data row1 col2" >0.026%</td>
      <td id="T_6ac90_row1_col3" class="data row1 col3" >0.022%</td>
      <td id="T_6ac90_row1_col4" class="data row1 col4" >0.012%</td>
      <td id="T_6ac90_row1_col5" class="data row1 col5" >0.010%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row2" class="row_heading level0 row2" >SecureRandom</th>
      <td id="T_6ac90_row2_col0" class="data row2 col0" >0.012%</td>
      <td id="T_6ac90_row2_col1" class="data row2 col1" >0.011%</td>
      <td id="T_6ac90_row2_col2" class="data row2 col2" >0.018%</td>
      <td id="T_6ac90_row2_col3" class="data row2 col3" >0.016%</td>
      <td id="T_6ac90_row2_col4" class="data row2 col4" >0.008%</td>
      <td id="T_6ac90_row2_col5" class="data row2 col5" >0.007%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row3" class="row_heading level0 row3" >Well512a</th>
      <td id="T_6ac90_row3_col0" class="data row3 col0" >0.006%</td>
      <td id="T_6ac90_row3_col1" class="data row3 col1" >0.005%</td>
      <td id="T_6ac90_row3_col2" class="data row3 col2" >0.002%</td>
      <td id="T_6ac90_row3_col3" class="data row3 col3" >0.001%</td>
      <td id="T_6ac90_row3_col4" class="data row3 col4" >0.011%</td>
      <td id="T_6ac90_row3_col5" class="data row3 col5" >0.009%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row4" class="row_heading level0 row4" >Well1024a</th>
      <td id="T_6ac90_row4_col0" class="data row4 col0" >0.002%</td>
      <td id="T_6ac90_row4_col1" class="data row4 col1" >0.002%</td>
      <td id="T_6ac90_row4_col2" class="data row4 col2" >0.009%</td>
      <td id="T_6ac90_row4_col3" class="data row4 col3" >0.008%</td>
      <td id="T_6ac90_row4_col4" class="data row4 col4" >0.011%</td>
      <td id="T_6ac90_row4_col5" class="data row4 col5" >0.010%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row5" class="row_heading level0 row5" >Well19937a</th>
      <td id="T_6ac90_row5_col0" class="data row5 col0" >0.006%</td>
      <td id="T_6ac90_row5_col1" class="data row5 col1" >0.005%</td>
      <td id="T_6ac90_row5_col2" class="data row5 col2" >0.024%</td>
      <td id="T_6ac90_row5_col3" class="data row5 col3" >0.021%</td>
      <td id="T_6ac90_row5_col4" class="data row5 col4" >0.023%</td>
      <td id="T_6ac90_row5_col5" class="data row5 col5" >0.020%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row6" class="row_heading level0 row6" >Well19937c</th>
      <td id="T_6ac90_row6_col0" class="data row6 col0" >0.003%</td>
      <td id="T_6ac90_row6_col1" class="data row6 col1" >0.003%</td>
      <td id="T_6ac90_row6_col2" class="data row6 col2" >0.012%</td>
      <td id="T_6ac90_row6_col3" class="data row6 col3" >0.010%</td>
      <td id="T_6ac90_row6_col4" class="data row6 col4" >0.021%</td>
      <td id="T_6ac90_row6_col5" class="data row6 col5" >0.018%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row7" class="row_heading level0 row7" >Well44497a</th>
      <td id="T_6ac90_row7_col0" class="data row7 col0" >0.005%</td>
      <td id="T_6ac90_row7_col1" class="data row7 col1" >0.005%</td>
      <td id="T_6ac90_row7_col2" class="data row7 col2" >0.048%</td>
      <td id="T_6ac90_row7_col3" class="data row7 col3" >0.041%</td>
      <td id="T_6ac90_row7_col4" class="data row7 col4" >0.005%</td>
      <td id="T_6ac90_row7_col5" class="data row7 col5" >0.004%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row8" class="row_heading level0 row8" >Well44497b</th>
      <td id="T_6ac90_row8_col0" class="data row8 col0" >0.009%</td>
      <td id="T_6ac90_row8_col1" class="data row8 col1" >0.008%</td>
      <td id="T_6ac90_row8_col2" class="data row8 col2" >0.010%</td>
      <td id="T_6ac90_row8_col3" class="data row8 col3" >0.009%</td>
      <td id="T_6ac90_row8_col4" class="data row8 col4" >0.013%</td>
      <td id="T_6ac90_row8_col5" class="data row8 col5" >0.011%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row9" class="row_heading level0 row9" >MersenneTwister</th>
      <td id="T_6ac90_row9_col0" class="data row9 col0" >0.019%</td>
      <td id="T_6ac90_row9_col1" class="data row9 col1" >0.017%</td>
      <td id="T_6ac90_row9_col2" class="data row9 col2" >0.002%</td>
      <td id="T_6ac90_row9_col3" class="data row9 col3" >0.001%</td>
      <td id="T_6ac90_row9_col4" class="data row9 col4" >0.005%</td>
      <td id="T_6ac90_row9_col5" class="data row9 col5" >0.004%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row10" class="row_heading level0 row10" >SFC64</th>
      <td id="T_6ac90_row10_col0" class="data row10 col0" >0.007%</td>
      <td id="T_6ac90_row10_col1" class="data row10 col1" >0.006%</td>
      <td id="T_6ac90_row10_col2" class="data row10 col2" >0.035%</td>
      <td id="T_6ac90_row10_col3" class="data row10 col3" >0.030%</td>
      <td id="T_6ac90_row10_col4" class="data row10 col4" >0.041%</td>
      <td id="T_6ac90_row10_col5" class="data row10 col5" >0.035%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row11" class="row_heading level0 row11" >ISAAC</th>
      <td id="T_6ac90_row11_col0" class="data row11 col0" >0.022%</td>
      <td id="T_6ac90_row11_col1" class="data row11 col1" >0.020%</td>
      <td id="T_6ac90_row11_col2" class="data row11 col2" >0.030%</td>
      <td id="T_6ac90_row11_col3" class="data row11 col3" >0.026%</td>
      <td id="T_6ac90_row11_col4" class="data row11 col4" >0.018%</td>
      <td id="T_6ac90_row11_col5" class="data row11 col5" >0.015%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row12" class="row_heading level0 row12" >XoRoShiRo128++</th>
      <td id="T_6ac90_row12_col0" class="data row12 col0" >0.004%</td>
      <td id="T_6ac90_row12_col1" class="data row12 col1" >0.004%</td>
      <td id="T_6ac90_row12_col2" class="data row12 col2" >0.008%</td>
      <td id="T_6ac90_row12_col3" class="data row12 col3" >0.007%</td>
      <td id="T_6ac90_row12_col4" class="data row12 col4" >0.006%</td>
      <td id="T_6ac90_row12_col5" class="data row12 col5" >0.005%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row13" class="row_heading level0 row13" >XoRoShiRo128**</th>
      <td id="T_6ac90_row13_col0" class="data row13 col0" >0.009%</td>
      <td id="T_6ac90_row13_col1" class="data row13 col1" >0.008%</td>
      <td id="T_6ac90_row13_col2" class="data row13 col2" >0.007%</td>
      <td id="T_6ac90_row13_col3" class="data row13 col3" >0.006%</td>
      <td id="T_6ac90_row13_col4" class="data row13 col4" >0.022%</td>
      <td id="T_6ac90_row13_col5" class="data row13 col5" >0.019%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row14" class="row_heading level0 row14" >XoRoShiRo64**</th>
      <td id="T_6ac90_row14_col0" class="data row14 col0" >0.011%</td>
      <td id="T_6ac90_row14_col1" class="data row14 col1" >0.010%</td>
      <td id="T_6ac90_row14_col2" class="data row14 col2" >0.012%</td>
      <td id="T_6ac90_row14_col3" class="data row14 col3" >0.011%</td>
      <td id="T_6ac90_row14_col4" class="data row14 col4" >0.008%</td>
      <td id="T_6ac90_row14_col5" class="data row14 col5" >0.006%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row15" class="row_heading level0 row15" >XoRoShiRo256++</th>
      <td id="T_6ac90_row15_col0" class="data row15 col0" >0.026%</td>
      <td id="T_6ac90_row15_col1" class="data row15 col1" >0.023%</td>
      <td id="T_6ac90_row15_col2" class="data row15 col2" >0.005%</td>
      <td id="T_6ac90_row15_col3" class="data row15 col3" >0.004%</td>
      <td id="T_6ac90_row15_col4" class="data row15 col4" >0.020%</td>
      <td id="T_6ac90_row15_col5" class="data row15 col5" >0.017%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row16" class="row_heading level0 row16" >XoRoShiRo1024++</th>
      <td id="T_6ac90_row16_col0" class="data row16 col0" >0.027%</td>
      <td id="T_6ac90_row16_col1" class="data row16 col1" >0.025%</td>
      <td id="T_6ac90_row16_col2" class="data row16 col2" >0.000%</td>
      <td id="T_6ac90_row16_col3" class="data row16 col3" >0.000%</td>
      <td id="T_6ac90_row16_col4" class="data row16 col4" >0.016%</td>
      <td id="T_6ac90_row16_col5" class="data row16 col5" >0.014%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row17" class="row_heading level0 row17" >XoRoShiRo1024*</th>
      <td id="T_6ac90_row17_col0" class="data row17 col0" >0.026%</td>
      <td id="T_6ac90_row17_col1" class="data row17 col1" >0.023%</td>
      <td id="T_6ac90_row17_col2" class="data row17 col2" >0.005%</td>
      <td id="T_6ac90_row17_col3" class="data row17 col3" >0.004%</td>
      <td id="T_6ac90_row17_col4" class="data row17 col4" >0.009%</td>
      <td id="T_6ac90_row17_col5" class="data row17 col5" >0.008%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row18" class="row_heading level0 row18" >XoRoShiRo1024**</th>
      <td id="T_6ac90_row18_col0" class="data row18 col0" >0.015%</td>
      <td id="T_6ac90_row18_col1" class="data row18 col1" >0.013%</td>
      <td id="T_6ac90_row18_col2" class="data row18 col2" >0.005%</td>
      <td id="T_6ac90_row18_col3" class="data row18 col3" >0.004%</td>
      <td id="T_6ac90_row18_col4" class="data row18 col4" >0.002%</td>
      <td id="T_6ac90_row18_col5" class="data row18 col5" >0.001%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row19" class="row_heading level0 row19" >L32X64Mix</th>
      <td id="T_6ac90_row19_col0" class="data row19 col0" >0.046%</td>
      <td id="T_6ac90_row19_col1" class="data row19 col1" >0.042%</td>
      <td id="T_6ac90_row19_col2" class="data row19 col2" >0.010%</td>
      <td id="T_6ac90_row19_col3" class="data row19 col3" >0.008%</td>
      <td id="T_6ac90_row19_col4" class="data row19 col4" >0.006%</td>
      <td id="T_6ac90_row19_col5" class="data row19 col5" >0.005%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row20" class="row_heading level0 row20" >L64X128Mix</th>
      <td id="T_6ac90_row20_col0" class="data row20 col0" >0.002%</td>
      <td id="T_6ac90_row20_col1" class="data row20 col1" >0.002%</td>
      <td id="T_6ac90_row20_col2" class="data row20 col2" >0.006%</td>
      <td id="T_6ac90_row20_col3" class="data row20 col3" >0.005%</td>
      <td id="T_6ac90_row20_col4" class="data row20 col4" >0.025%</td>
      <td id="T_6ac90_row20_col5" class="data row20 col5" >0.021%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row21" class="row_heading level0 row21" >L64X128**</th>
      <td id="T_6ac90_row21_col0" class="data row21 col0" >0.013%</td>
      <td id="T_6ac90_row21_col1" class="data row21 col1" >0.012%</td>
      <td id="T_6ac90_row21_col2" class="data row21 col2" >0.005%</td>
      <td id="T_6ac90_row21_col3" class="data row21 col3" >0.004%</td>
      <td id="T_6ac90_row21_col4" class="data row21 col4" >0.006%</td>
      <td id="T_6ac90_row21_col5" class="data row21 col5" >0.005%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row22" class="row_heading level0 row22" >L64X256Mix</th>
      <td id="T_6ac90_row22_col0" class="data row22 col0" >0.020%</td>
      <td id="T_6ac90_row22_col1" class="data row22 col1" >0.018%</td>
      <td id="T_6ac90_row22_col2" class="data row22 col2" >0.002%</td>
      <td id="T_6ac90_row22_col3" class="data row22 col3" >0.002%</td>
      <td id="T_6ac90_row22_col4" class="data row22 col4" >0.002%</td>
      <td id="T_6ac90_row22_col5" class="data row22 col5" >0.002%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row23" class="row_heading level0 row23" >L64X1024Mix</th>
      <td id="T_6ac90_row23_col0" class="data row23 col0" >0.046%</td>
      <td id="T_6ac90_row23_col1" class="data row23 col1" >0.041%</td>
      <td id="T_6ac90_row23_col2" class="data row23 col2" >0.009%</td>
      <td id="T_6ac90_row23_col3" class="data row23 col3" >0.008%</td>
      <td id="T_6ac90_row23_col4" class="data row23 col4" >0.035%</td>
      <td id="T_6ac90_row23_col5" class="data row23 col5" >0.029%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row24" class="row_heading level0 row24" >L128X128Mix</th>
      <td id="T_6ac90_row24_col0" class="data row24 col0" >0.017%</td>
      <td id="T_6ac90_row24_col1" class="data row24 col1" >0.015%</td>
      <td id="T_6ac90_row24_col2" class="data row24 col2" >0.033%</td>
      <td id="T_6ac90_row24_col3" class="data row24 col3" >0.028%</td>
      <td id="T_6ac90_row24_col4" class="data row24 col4" >0.040%</td>
      <td id="T_6ac90_row24_col5" class="data row24 col5" >0.034%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row25" class="row_heading level0 row25" >L128X256Mix</th>
      <td id="T_6ac90_row25_col0" class="data row25 col0" >0.007%</td>
      <td id="T_6ac90_row25_col1" class="data row25 col1" >0.006%</td>
      <td id="T_6ac90_row25_col2" class="data row25 col2" >0.013%</td>
      <td id="T_6ac90_row25_col3" class="data row25 col3" >0.011%</td>
      <td id="T_6ac90_row25_col4" class="data row25 col4" >0.001%</td>
      <td id="T_6ac90_row25_col5" class="data row25 col5" >0.001%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row26" class="row_heading level0 row26" >L128X1024Mix</th>
      <td id="T_6ac90_row26_col0" class="data row26 col0" >0.018%</td>
      <td id="T_6ac90_row26_col1" class="data row26 col1" >0.016%</td>
      <td id="T_6ac90_row26_col2" class="data row26 col2" >0.016%</td>
      <td id="T_6ac90_row26_col3" class="data row26 col3" >0.014%</td>
      <td id="T_6ac90_row26_col4" class="data row26 col4" >0.007%</td>
      <td id="T_6ac90_row26_col5" class="data row26 col5" >0.006%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row27" class="row_heading level0 row27" >PcgRxsMXs64</th>
      <td id="T_6ac90_row27_col0" class="data row27 col0" >0.010%</td>
      <td id="T_6ac90_row27_col1" class="data row27 col1" >0.009%</td>
      <td id="T_6ac90_row27_col2" class="data row27 col2" >0.000%</td>
      <td id="T_6ac90_row27_col3" class="data row27 col3" >0.000%</td>
      <td id="T_6ac90_row27_col4" class="data row27 col4" >0.036%</td>
      <td id="T_6ac90_row27_col5" class="data row27 col5" >0.030%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row28" class="row_heading level0 row28" >Philox4x64</th>
      <td id="T_6ac90_row28_col0" class="data row28 col0" >0.016%</td>
      <td id="T_6ac90_row28_col1" class="data row28 col1" >0.015%</td>
      <td id="T_6ac90_row28_col2" class="data row28 col2" >0.001%</td>
      <td id="T_6ac90_row28_col3" class="data row28 col3" >0.001%</td>
      <td id="T_6ac90_row28_col4" class="data row28 col4" >0.007%</td>
      <td id="T_6ac90_row28_col5" class="data row28 col5" >0.006%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row29" class="row_heading level0 row29" >Drand48</th>
      <td id="T_6ac90_row29_col0" class="data row29 col0" >0.044%</td>
      <td id="T_6ac90_row29_col1" class="data row29 col1" >0.040%</td>
      <td id="T_6ac90_row29_col2" class="data row29 col2" >0.023%</td>
      <td id="T_6ac90_row29_col3" class="data row29 col3" >0.019%</td>
      <td id="T_6ac90_row29_col4" class="data row29 col4" >0.044%</td>
      <td id="T_6ac90_row29_col5" class="data row29 col5" >0.037%</td>
    </tr>
    <tr>
      <th id="T_6ac90_level0_row30" class="row_heading level0 row30" >Drand48Mix</th>
      <td id="T_6ac90_row30_col0" class="data row30 col0" >0.083%</td>
      <td id="T_6ac90_row30_col1" class="data row30 col1" >0.075%</td>
      <td id="T_6ac90_row30_col2" class="data row30 col2" >0.079%</td>
      <td id="T_6ac90_row30_col3" class="data row30 col3" >0.067%</td>
      <td id="T_6ac90_row30_col4" class="data row30 col4" >0.014%</td>
      <td id="T_6ac90_row30_col5" class="data row30 col5" >0.012%</td>
    </tr>
  </tbody>
</table>

### M/M/1 and M/G/1 - $\rho=95\,\%$

<table id="T_3702d">
  <caption>Mean Error (in \%)</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_3702d_level0_col0" class="col_heading level0 col0" >E[W] - MM1</th>
      <th id="T_3702d_level0_col1" class="col_heading level0 col1" >E[V] - MM1</th>
      <th id="T_3702d_level0_col2" class="col_heading level0 col2" >E[W] - MG1Log</th>
      <th id="T_3702d_level0_col3" class="col_heading level0 col3" >E[V] - MG1Log</th>
      <th id="T_3702d_level0_col4" class="col_heading level0 col4" >E[W] - MG1Gamma</th>
      <th id="T_3702d_level0_col5" class="col_heading level0 col5" >E[V] - MG1Gamma</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_3702d_level0_row0" class="row_heading level0 row0" >ThreadLocalRandom</th>
      <td id="T_3702d_row0_col0" class="data row0 col0" >122.823%</td>
      <td id="T_3702d_row0_col1" class="data row0 col1" >111.096%</td>
      <td id="T_3702d_row0_col2" class="data row0 col2" >118.209%</td>
      <td id="T_3702d_row0_col3" class="data row0 col3" >101.205%</td>
      <td id="T_3702d_row0_col4" class="data row0 col4" >118.157%</td>
      <td id="T_3702d_row0_col5" class="data row0 col5" >101.161%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row1" class="row_heading level0 row1" >Random</th>
      <td id="T_3702d_row1_col0" class="data row1 col0" >122.729%</td>
      <td id="T_3702d_row1_col1" class="data row1 col1" >111.012%</td>
      <td id="T_3702d_row1_col2" class="data row1 col2" >118.247%</td>
      <td id="T_3702d_row1_col3" class="data row1 col3" >101.237%</td>
      <td id="T_3702d_row1_col4" class="data row1 col4" >118.192%</td>
      <td id="T_3702d_row1_col5" class="data row1 col5" >101.191%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row2" class="row_heading level0 row2" >SecureRandom</th>
      <td id="T_3702d_row2_col0" class="data row2 col0" >122.962%</td>
      <td id="T_3702d_row2_col1" class="data row2 col1" >111.222%</td>
      <td id="T_3702d_row2_col2" class="data row2 col2" >118.265%</td>
      <td id="T_3702d_row2_col3" class="data row2 col3" >101.252%</td>
      <td id="T_3702d_row2_col4" class="data row2 col4" >118.211%</td>
      <td id="T_3702d_row2_col5" class="data row2 col5" >101.206%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row3" class="row_heading level0 row3" >Well512a</th>
      <td id="T_3702d_row3_col0" class="data row3 col0" >123.060%</td>
      <td id="T_3702d_row3_col1" class="data row3 col1" >111.310%</td>
      <td id="T_3702d_row3_col2" class="data row3 col2" >118.252%</td>
      <td id="T_3702d_row3_col3" class="data row3 col3" >101.241%</td>
      <td id="T_3702d_row3_col4" class="data row3 col4" >118.363%</td>
      <td id="T_3702d_row3_col5" class="data row3 col5" >101.336%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row4" class="row_heading level0 row4" >Well1024a</th>
      <td id="T_3702d_row4_col0" class="data row4 col0" >122.718%</td>
      <td id="T_3702d_row4_col1" class="data row4 col1" >111.002%</td>
      <td id="T_3702d_row4_col2" class="data row4 col2" >118.254%</td>
      <td id="T_3702d_row4_col3" class="data row4 col3" >101.242%</td>
      <td id="T_3702d_row4_col4" class="data row4 col4" >118.243%</td>
      <td id="T_3702d_row4_col5" class="data row4 col5" >101.234%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row5" class="row_heading level0 row5" >Well19937a</th>
      <td id="T_3702d_row5_col0" class="data row5 col0" >122.807%</td>
      <td id="T_3702d_row5_col1" class="data row5 col1" >111.082%</td>
      <td id="T_3702d_row5_col2" class="data row5 col2" >118.218%</td>
      <td id="T_3702d_row5_col3" class="data row5 col3" >101.212%</td>
      <td id="T_3702d_row5_col4" class="data row5 col4" >118.140%</td>
      <td id="T_3702d_row5_col5" class="data row5 col5" >101.146%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row6" class="row_heading level0 row6" >Well19937c</th>
      <td id="T_3702d_row6_col0" class="data row6 col0" >122.897%</td>
      <td id="T_3702d_row6_col1" class="data row6 col1" >111.164%</td>
      <td id="T_3702d_row6_col2" class="data row6 col2" >118.338%</td>
      <td id="T_3702d_row6_col3" class="data row6 col3" >101.315%</td>
      <td id="T_3702d_row6_col4" class="data row6 col4" >118.141%</td>
      <td id="T_3702d_row6_col5" class="data row6 col5" >101.147%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row7" class="row_heading level0 row7" >Well44497a</th>
      <td id="T_3702d_row7_col0" class="data row7 col0" >122.865%</td>
      <td id="T_3702d_row7_col1" class="data row7 col1" >111.134%</td>
      <td id="T_3702d_row7_col2" class="data row7 col2" >118.221%</td>
      <td id="T_3702d_row7_col3" class="data row7 col3" >101.214%</td>
      <td id="T_3702d_row7_col4" class="data row7 col4" >118.210%</td>
      <td id="T_3702d_row7_col5" class="data row7 col5" >101.206%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row8" class="row_heading level0 row8" >Well44497b</th>
      <td id="T_3702d_row8_col0" class="data row8 col0" >122.891%</td>
      <td id="T_3702d_row8_col1" class="data row8 col1" >111.158%</td>
      <td id="T_3702d_row8_col2" class="data row8 col2" >118.167%</td>
      <td id="T_3702d_row8_col3" class="data row8 col3" >101.169%</td>
      <td id="T_3702d_row8_col4" class="data row8 col4" >118.200%</td>
      <td id="T_3702d_row8_col5" class="data row8 col5" >101.197%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row9" class="row_heading level0 row9" >MersenneTwister</th>
      <td id="T_3702d_row9_col0" class="data row9 col0" >122.860%</td>
      <td id="T_3702d_row9_col1" class="data row9 col1" >111.129%</td>
      <td id="T_3702d_row9_col2" class="data row9 col2" >118.246%</td>
      <td id="T_3702d_row9_col3" class="data row9 col3" >101.237%</td>
      <td id="T_3702d_row9_col4" class="data row9 col4" >118.204%</td>
      <td id="T_3702d_row9_col5" class="data row9 col5" >101.200%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row10" class="row_heading level0 row10" >SFC64</th>
      <td id="T_3702d_row10_col0" class="data row10 col0" >122.748%</td>
      <td id="T_3702d_row10_col1" class="data row10 col1" >111.029%</td>
      <td id="T_3702d_row10_col2" class="data row10 col2" >118.248%</td>
      <td id="T_3702d_row10_col3" class="data row10 col3" >101.237%</td>
      <td id="T_3702d_row10_col4" class="data row10 col4" >118.220%</td>
      <td id="T_3702d_row10_col5" class="data row10 col5" >101.214%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row11" class="row_heading level0 row11" >ISAAC</th>
      <td id="T_3702d_row11_col0" class="data row11 col0" >122.859%</td>
      <td id="T_3702d_row11_col1" class="data row11 col1" >111.128%</td>
      <td id="T_3702d_row11_col2" class="data row11 col2" >118.293%</td>
      <td id="T_3702d_row11_col3" class="data row11 col3" >101.276%</td>
      <td id="T_3702d_row11_col4" class="data row11 col4" >118.312%</td>
      <td id="T_3702d_row11_col5" class="data row11 col5" >101.292%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row12" class="row_heading level0 row12" >XoRoShiRo128++</th>
      <td id="T_3702d_row12_col0" class="data row12 col0" >122.870%</td>
      <td id="T_3702d_row12_col1" class="data row12 col1" >111.138%</td>
      <td id="T_3702d_row12_col2" class="data row12 col2" >118.197%</td>
      <td id="T_3702d_row12_col3" class="data row12 col3" >101.194%</td>
      <td id="T_3702d_row12_col4" class="data row12 col4" >118.297%</td>
      <td id="T_3702d_row12_col5" class="data row12 col5" >101.280%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row13" class="row_heading level0 row13" >XoRoShiRo128**</th>
      <td id="T_3702d_row13_col0" class="data row13 col0" >122.761%</td>
      <td id="T_3702d_row13_col1" class="data row13 col1" >111.040%</td>
      <td id="T_3702d_row13_col2" class="data row13 col2" >118.189%</td>
      <td id="T_3702d_row13_col3" class="data row13 col3" >101.188%</td>
      <td id="T_3702d_row13_col4" class="data row13 col4" >118.442%</td>
      <td id="T_3702d_row13_col5" class="data row13 col5" >101.403%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row14" class="row_heading level0 row14" >XoRoShiRo64**</th>
      <td id="T_3702d_row14_col0" class="data row14 col0" >122.805%</td>
      <td id="T_3702d_row14_col1" class="data row14 col1" >111.081%</td>
      <td id="T_3702d_row14_col2" class="data row14 col2" >118.200%</td>
      <td id="T_3702d_row14_col3" class="data row14 col3" >101.197%</td>
      <td id="T_3702d_row14_col4" class="data row14 col4" >118.303%</td>
      <td id="T_3702d_row14_col5" class="data row14 col5" >101.284%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row15" class="row_heading level0 row15" >XoRoShiRo256++</th>
      <td id="T_3702d_row15_col0" class="data row15 col0" >122.822%</td>
      <td id="T_3702d_row15_col1" class="data row15 col1" >111.095%</td>
      <td id="T_3702d_row15_col2" class="data row15 col2" >118.335%</td>
      <td id="T_3702d_row15_col3" class="data row15 col3" >101.312%</td>
      <td id="T_3702d_row15_col4" class="data row15 col4" >118.277%</td>
      <td id="T_3702d_row15_col5" class="data row15 col5" >101.263%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row16" class="row_heading level0 row16" >XoRoShiRo1024++</th>
      <td id="T_3702d_row16_col0" class="data row16 col0" >122.970%</td>
      <td id="T_3702d_row16_col1" class="data row16 col1" >111.228%</td>
      <td id="T_3702d_row16_col2" class="data row16 col2" >118.408%</td>
      <td id="T_3702d_row16_col3" class="data row16 col3" >101.374%</td>
      <td id="T_3702d_row16_col4" class="data row16 col4" >118.360%</td>
      <td id="T_3702d_row16_col5" class="data row16 col5" >101.333%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row17" class="row_heading level0 row17" >XoRoShiRo1024*</th>
      <td id="T_3702d_row17_col0" class="data row17 col0" >122.814%</td>
      <td id="T_3702d_row17_col1" class="data row17 col1" >111.088%</td>
      <td id="T_3702d_row17_col2" class="data row17 col2" >118.268%</td>
      <td id="T_3702d_row17_col3" class="data row17 col3" >101.255%</td>
      <td id="T_3702d_row17_col4" class="data row17 col4" >118.285%</td>
      <td id="T_3702d_row17_col5" class="data row17 col5" >101.269%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row18" class="row_heading level0 row18" >XoRoShiRo1024**</th>
      <td id="T_3702d_row18_col0" class="data row18 col0" >122.806%</td>
      <td id="T_3702d_row18_col1" class="data row18 col1" >111.081%</td>
      <td id="T_3702d_row18_col2" class="data row18 col2" >118.293%</td>
      <td id="T_3702d_row18_col3" class="data row18 col3" >101.276%</td>
      <td id="T_3702d_row18_col4" class="data row18 col4" >118.141%</td>
      <td id="T_3702d_row18_col5" class="data row18 col5" >101.147%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row19" class="row_heading level0 row19" >L32X64Mix</th>
      <td id="T_3702d_row19_col0" class="data row19 col0" >122.912%</td>
      <td id="T_3702d_row19_col1" class="data row19 col1" >111.177%</td>
      <td id="T_3702d_row19_col2" class="data row19 col2" >118.192%</td>
      <td id="T_3702d_row19_col3" class="data row19 col3" >101.190%</td>
      <td id="T_3702d_row19_col4" class="data row19 col4" >118.351%</td>
      <td id="T_3702d_row19_col5" class="data row19 col5" >101.325%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row20" class="row_heading level0 row20" >L64X128Mix</th>
      <td id="T_3702d_row20_col0" class="data row20 col0" >122.876%</td>
      <td id="T_3702d_row20_col1" class="data row20 col1" >111.144%</td>
      <td id="T_3702d_row20_col2" class="data row20 col2" >118.282%</td>
      <td id="T_3702d_row20_col3" class="data row20 col3" >101.267%</td>
      <td id="T_3702d_row20_col4" class="data row20 col4" >118.252%</td>
      <td id="T_3702d_row20_col5" class="data row20 col5" >101.241%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row21" class="row_heading level0 row21" >L64X128**</th>
      <td id="T_3702d_row21_col0" class="data row21 col0" >122.833%</td>
      <td id="T_3702d_row21_col1" class="data row21 col1" >111.105%</td>
      <td id="T_3702d_row21_col2" class="data row21 col2" >118.245%</td>
      <td id="T_3702d_row21_col3" class="data row21 col3" >101.235%</td>
      <td id="T_3702d_row21_col4" class="data row21 col4" >118.266%</td>
      <td id="T_3702d_row21_col5" class="data row21 col5" >101.253%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row22" class="row_heading level0 row22" >L64X256Mix</th>
      <td id="T_3702d_row22_col0" class="data row22 col0" >122.768%</td>
      <td id="T_3702d_row22_col1" class="data row22 col1" >111.047%</td>
      <td id="T_3702d_row22_col2" class="data row22 col2" >118.344%</td>
      <td id="T_3702d_row22_col3" class="data row22 col3" >101.319%</td>
      <td id="T_3702d_row22_col4" class="data row22 col4" >118.337%</td>
      <td id="T_3702d_row22_col5" class="data row22 col5" >101.314%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row23" class="row_heading level0 row23" >L64X1024Mix</th>
      <td id="T_3702d_row23_col0" class="data row23 col0" >122.669%</td>
      <td id="T_3702d_row23_col1" class="data row23 col1" >110.958%</td>
      <td id="T_3702d_row23_col2" class="data row23 col2" >118.243%</td>
      <td id="T_3702d_row23_col3" class="data row23 col3" >101.234%</td>
      <td id="T_3702d_row23_col4" class="data row23 col4" >118.225%</td>
      <td id="T_3702d_row23_col5" class="data row23 col5" >101.219%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row24" class="row_heading level0 row24" >L128X128Mix</th>
      <td id="T_3702d_row24_col0" class="data row24 col0" >122.849%</td>
      <td id="T_3702d_row24_col1" class="data row24 col1" >111.120%</td>
      <td id="T_3702d_row24_col2" class="data row24 col2" >118.310%</td>
      <td id="T_3702d_row24_col3" class="data row24 col3" >101.291%</td>
      <td id="T_3702d_row24_col4" class="data row24 col4" >118.282%</td>
      <td id="T_3702d_row24_col5" class="data row24 col5" >101.267%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row25" class="row_heading level0 row25" >L128X256Mix</th>
      <td id="T_3702d_row25_col0" class="data row25 col0" >122.764%</td>
      <td id="T_3702d_row25_col1" class="data row25 col1" >111.043%</td>
      <td id="T_3702d_row25_col2" class="data row25 col2" >118.342%</td>
      <td id="T_3702d_row25_col3" class="data row25 col3" >101.317%</td>
      <td id="T_3702d_row25_col4" class="data row25 col4" >118.328%</td>
      <td id="T_3702d_row25_col5" class="data row25 col5" >101.305%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row26" class="row_heading level0 row26" >L128X1024Mix</th>
      <td id="T_3702d_row26_col0" class="data row26 col0" >122.803%</td>
      <td id="T_3702d_row26_col1" class="data row26 col1" >111.078%</td>
      <td id="T_3702d_row26_col2" class="data row26 col2" >118.301%</td>
      <td id="T_3702d_row26_col3" class="data row26 col3" >101.283%</td>
      <td id="T_3702d_row26_col4" class="data row26 col4" >118.257%</td>
      <td id="T_3702d_row26_col5" class="data row26 col5" >101.245%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row27" class="row_heading level0 row27" >PcgRxsMXs64</th>
      <td id="T_3702d_row27_col0" class="data row27 col0" >122.753%</td>
      <td id="T_3702d_row27_col1" class="data row27 col1" >111.033%</td>
      <td id="T_3702d_row27_col2" class="data row27 col2" >118.259%</td>
      <td id="T_3702d_row27_col3" class="data row27 col3" >101.247%</td>
      <td id="T_3702d_row27_col4" class="data row27 col4" >118.224%</td>
      <td id="T_3702d_row27_col5" class="data row27 col5" >101.217%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row28" class="row_heading level0 row28" >Philox4x64</th>
      <td id="T_3702d_row28_col0" class="data row28 col0" >122.929%</td>
      <td id="T_3702d_row28_col1" class="data row28 col1" >111.192%</td>
      <td id="T_3702d_row28_col2" class="data row28 col2" >118.221%</td>
      <td id="T_3702d_row28_col3" class="data row28 col3" >101.215%</td>
      <td id="T_3702d_row28_col4" class="data row28 col4" >118.260%</td>
      <td id="T_3702d_row28_col5" class="data row28 col5" >101.248%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row29" class="row_heading level0 row29" >Drand48</th>
      <td id="T_3702d_row29_col0" class="data row29 col0" >122.744%</td>
      <td id="T_3702d_row29_col1" class="data row29 col1" >111.025%</td>
      <td id="T_3702d_row29_col2" class="data row29 col2" >118.411%</td>
      <td id="T_3702d_row29_col3" class="data row29 col3" >101.376%</td>
      <td id="T_3702d_row29_col4" class="data row29 col4" >117.992%</td>
      <td id="T_3702d_row29_col5" class="data row29 col5" >101.020%</td>
    </tr>
    <tr>
      <th id="T_3702d_level0_row30" class="row_heading level0 row30" >Drand48Mix</th>
      <td id="T_3702d_row30_col0" class="data row30 col0" >122.704%</td>
      <td id="T_3702d_row30_col1" class="data row30 col1" >110.989%</td>
      <td id="T_3702d_row30_col2" class="data row30 col2" >118.069%</td>
      <td id="T_3702d_row30_col3" class="data row30 col3" >101.086%</td>
      <td id="T_3702d_row30_col4" class="data row30 col4" >118.365%</td>
      <td id="T_3702d_row30_col5" class="data row30 col5" >101.337%</td>
    </tr>
  </tbody>
</table>

### Boxplots of the relative errors

![Boxplots of the relative errors of the different pseudorandom number generators](plot2.png)

### Parameter series: Changing &rho; from 60% up to 98%

M/G/1 model (S=log-normal) - relative errors of E[W] (using Pollaczek-Khintchine formula for exact results)

![Relative errors of E[W]](plot2rho.png)

### Maximum absolute relative errors of E[W]

<table id="T_79811">
  <caption>Max Relative Error (in \%)</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_79811_level0_col0" class="col_heading level0 col0" >max_rel_error</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_79811_level0_row0" class="row_heading level0 row0" >ThreadLocalRandom</th>
      <td id="T_79811_row0_col0" class="data row0 col0" >0.226%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row1" class="row_heading level0 row1" >Random</th>
      <td id="T_79811_row1_col0" class="data row1 col0" >0.153%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row2" class="row_heading level0 row2" >SecureRandom</th>
      <td id="T_79811_row2_col0" class="data row2 col0" >0.183%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row3" class="row_heading level0 row3" >Well512a</th>
      <td id="T_79811_row3_col0" class="data row3 col0" >0.242%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row4" class="row_heading level0 row4" >Well1024a</th>
      <td id="T_79811_row4_col0" class="data row4 col0" >0.340%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row5" class="row_heading level0 row5" >Well19937a</th>
      <td id="T_79811_row5_col0" class="data row5 col0" >0.343%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row6" class="row_heading level0 row6" >Well19937c</th>
      <td id="T_79811_row6_col0" class="data row6 col0" >0.302%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row7" class="row_heading level0 row7" >Well44497a</th>
      <td id="T_79811_row7_col0" class="data row7 col0" >0.354%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row8" class="row_heading level0 row8" >Well44497b</th>
      <td id="T_79811_row8_col0" class="data row8 col0" >0.126%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row9" class="row_heading level0 row9" >MersenneTwister</th>
      <td id="T_79811_row9_col0" class="data row9 col0" >0.268%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row10" class="row_heading level0 row10" >ISAAC</th>
      <td id="T_79811_row10_col0" class="data row10 col0" >0.161%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row11" class="row_heading level0 row11" >XoRoShiRo128++</th>
      <td id="T_79811_row11_col0" class="data row11 col0" >0.352%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row12" class="row_heading level0 row12" >XoRoShiRo128**</th>
      <td id="T_79811_row12_col0" class="data row12 col0" >0.249%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row13" class="row_heading level0 row13" >XoRoShiRo64**</th>
      <td id="T_79811_row13_col0" class="data row13 col0" >0.384%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row14" class="row_heading level0 row14" >L32X64Mix</th>
      <td id="T_79811_row14_col0" class="data row14 col0" >0.222%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row15" class="row_heading level0 row15" >Drand48</th>
      <td id="T_79811_row15_col0" class="data row15 col0" >1.335%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row16" class="row_heading level0 row16" >XoRoShiRo256++</th>
      <td id="T_79811_row16_col0" class="data row16 col0" >0.084%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row17" class="row_heading level0 row17" >L64X128Mix</th>
      <td id="T_79811_row17_col0" class="data row17 col0" >0.085%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row18" class="row_heading level0 row18" >L64X128**</th>
      <td id="T_79811_row18_col0" class="data row18 col0" >0.113%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row19" class="row_heading level0 row19" >L64X256Mix</th>
      <td id="T_79811_row19_col0" class="data row19 col0" >0.130%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row20" class="row_heading level0 row20" >L64X1024Mix</th>
      <td id="T_79811_row20_col0" class="data row20 col0" >0.048%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row21" class="row_heading level0 row21" >L128X128Mix</th>
      <td id="T_79811_row21_col0" class="data row21 col0" >0.078%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row22" class="row_heading level0 row22" >L128X256Mix</th>
      <td id="T_79811_row22_col0" class="data row22 col0" >0.109%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row23" class="row_heading level0 row23" >L128X1024Mix</th>
      <td id="T_79811_row23_col0" class="data row23 col0" >0.111%</td>
    </tr>
    <tr>
      <th id="T_79811_level0_row24" class="row_heading level0 row24" >Drand48Mix</th>
      <td id="T_79811_row24_col0" class="data row24 col0" >0.298%</td>
    </tr>
  </tbody>
</table>



## Model files

The simulation was based on these Warteschlangensimulator model files:

* [M/M/1 &rho;=90%](models/model2MM1rho90.xml)
* [M/M/1 &rho;=95%](models/model2MM1rho95.xml)
* [M/G/1 (S=log-normal) &rho;=90%](models/model2MG1LogRho90.xml)
* [M/G/1 (S=log-normal) &rho;=95%](models/model2MG1LogRho95.xml)
* [M/G/1 (S=gamma) &rho;=90%](models/model2MG1GammaRho90.xml)
* [M/G/1 (S=gamma) &rho;=95%](models/model2MG1GammaRho95.xml)

## Raw result data

Raw data from the simulations as tabulator separated text files:

* [M/M/1 &rho;=80%](statistics/results2MM1rho80.txt)
* [M/M/1 &rho;=90%](statistics/results2MM1rho90.txt)
* [M/M/1 &rho;=95%](statistics/results2MM1rho95.txt)
* [M/G/1 (S=log-normal) &rho;=90%](statistics/results2MG1LogRho90.txt)
* [M/G/1 (S=log-normal) &rho;=95%](statistics/results2MG1LogRho95.txt)
* [M/G/1 (S=gamma) &rho;=90%](statistics/results2MG1GammaRho90.txt)
* [M/G/1 (S=gamma) &rho;=95%](statistics/results2MG1GammaRho95.txt)
* [M/G/1 (S=log-normal) &rho;=60..98%](statistics/results2MG1Log-variatingRho.txt)
* [M/G/1 (S=gamma) &rho;=60..98%](statistics/results2MG1Gamma-variatingRho.txt)

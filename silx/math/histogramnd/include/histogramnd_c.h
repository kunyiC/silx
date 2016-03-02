#ifndef HISTOGRAMND_C_H
#define HISTOGRAMND_C_H

#include <inttypes.h>

#include "templates.h"

typedef enum {
    HISTO_NONE              = 0,
    HISTO_WEIGHT_MIN        = 1,
    HISTO_WEIGHT_MAX       = 1<<1,
    HISTO_LAST_BIN_CLOSED   = 1<<2
} histo_opt_type;

/*=====================
 * double sample
 * ====================
*/

int histogramnd_double_double(double *i_sample,
                                double *i_weigths,
                                int i_n_dim,
                                int i_n_elem,
                                double *i_bin_ranges,
                                int *i_n_bin,
                                uint32_t *o_histo,
                                double *o_cumul,
                                int i_opt_flags,
                                double i_weight_min,
                                double i_weight_max);
                                
int histogramnd_double_float(double *i_sample,
                                float *i_weigths,
                                int i_n_dim,
                                int i_n_elem,
                                double *i_bin_ranges,
                                int *i_n_bin,
                                uint32_t *o_histo,
                                double *o_cumul,
                                int i_opt_flags,
                                float i_weight_min,
                                float i_weight_max);
                                
int histogramnd_double_int32_t(double *i_sample,
                                int32_t *i_weigths,
                                int i_n_dim,
                                int i_n_elem,
                                double *i_bin_ranges,
                                int *i_n_bin,
                                uint32_t *o_histo,
                                double *o_cumul,
                                int i_opt_flags,
                                int32_t i_weight_min,
                                int32_t i_weight_max);
                        
/*=====================
 * float sample
 * ====================
*/
int histogramnd_float_double(float *i_sample,
                                double *i_weigths,
                                int i_n_dim,
                                int i_n_elem,
                                double *i_bin_ranges,
                                int *i_n_bin,
                                uint32_t *o_histo,
                                double *o_cumul,
                                int i_opt_flags,
                                double i_weight_min,
                                double i_weight_max);
                                
int histogramnd_float_float(float *i_sample,
                                float *i_weigths,
                                int i_n_dim,
                                int i_n_elem,
                                double *i_bin_ranges,
                                int *i_n_bin,
                                uint32_t *o_histo,
                                double *o_cumul,
                                int i_opt_flags,
                                float i_weight_min,
                                float i_weight_max);
                                
int histogramnd_float_int32_t(float *i_sample,
                                int32_t *i_weigths,
                                int i_n_dim,
                                int i_n_elem,
                                double *i_bin_ranges,
                                int *i_n_bin,
                                uint32_t *o_histo,
                                double *o_cumul,
                                int i_opt_flags,
                                int32_t i_weight_min,
                                int32_t i_weight_max);

/*=====================
 * int32_t sample
 * ====================
*/
int histogramnd_int32_t_double(int32_t *i_sample,
                                double *i_weigths,
                                int i_n_dim,
                                int i_n_elem,
                                double *i_bin_ranges,
                                int *i_n_bin,
                                uint32_t *o_histo,
                                double *o_cumul,
                                int i_opt_flags,
                                double i_weight_min,
                                double i_weight_max);
                                
int histogramnd_int32_t_float(int32_t *i_sample,
                                float *i_weigths,
                                int i_n_dim,
                                int i_n_elem,
                                double *i_bin_ranges,
                                int *i_n_bin,
                                uint32_t *o_histo,
                                double *o_cumul,
                                int i_opt_flags,
                                float i_weight_min,
                                float i_weight_max);
                                
int histogramnd_int32_t_int32_t(int32_t *i_sample,
                                int32_t *i_weigths,
                                int i_n_dim,
                                int i_n_elem,
                                double *i_bin_ranges,
                                int *i_n_bin,
                                uint32_t *o_histo,
                                double *o_cumul,
                                int i_opt_flags,
                                int32_t i_weight_min,
                                int32_t i_weight_max);
                        
#endif /* #define HISTOGRAMND_C_H */
